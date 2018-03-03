from sklearn.decomposition import PCA as sklearnPCA
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['usa_db']
collection = db['usa_tweets_collection']
tweets_iterator = collection.find()

i = 20000
location = []
for tweet in tweets_iterator:
  if i <= 1000:   
    if tweet['coordinates']:
      location.append(1)
    else:
      location.append(0)
  i-=1

print('location length = ', len(location))

df = pd.read_csv('emojis.csv')
num_vars = len(df.columns)
num_obs = len(df.iloc[:,0])

print()
print(num_obs)
print()

A = df.as_matrix()

U, S, V = np.linalg.svd(A)
eigvals = S**2 / np.cumsum(S)[-1]

fig = plt.figure(figsize=(8,5))
sing_vals = np.arange(num_vars) + 1
plt.plot(sing_vals, eigvals, 'ro-', linewidth=2)
plt.title('SVD Plot')
plt.xlabel('Principal Component')
plt.ylabel('Singular value')
leg = plt.legend(['Eigenvalues from SVD'], loc='best', borderpad=0.3, 
                 shadow=False, prop=matplotlib.font_manager.FontProperties(size='small'),
                 markerscale=0.4)
leg.get_frame().set_alpha(0.4)
leg.draggable(state=True)
plt.show()

sklearn_pca = sklearnPCA(n_components=12)
Y_sklearn = sklearn_pca.fit_transform(A)

#XY =  np.hstack((Y_sklearn, np.array(df.iloc[:, -1]).reshape(1000, 1)))

X = Y_sklearn
Y = np.array(location).reshape(4226, 1)

def sig(x):
    return 1/(1 + np.exp(-x))

def sigDiv(x):
    return sig(x)*(1-sig(x))

def NN3_sig(X, Y, stopWhen):
    print("--- Using activation function sig ---")
    print()
    colsize = len(list(X[1]))
    print('col = ', colsize)
    rowsize = len(list(X[:, 1]))
    print('row = ', rowsize)
    w0 = 2*np.random.random((colsize, colsize)) - 1
    w1 = 2*np.random.random((colsize, rowsize)) - 1
    w2 = 2*np.random.random((rowsize, 1)) - 1
    err = []
    
    while True:

        l0 = X
        l1 = sig(np.dot(l0, w0)) 
        l2 = sig(np.dot(l1, w1))
        l3 = sig(np.dot(l2, w2))

        l3_error = Y - l3

        if abs(np.mean(l3_error)) <= stopWhen:
            break
        
        l3_delta = l3_error * sigDiv(l3)
        l2_error = l3_delta.dot(w2.T)
        l2_delta = l2_error * sigDiv(l2)
        l1_error = l2_delta.dot(w1.T)
        l1_delta = l1_error * sigDiv(l1)
        
        err.append(np.mean(l3_error))

        if len(err) !=0 and len(err) %50 == 0:
            print(err[-1])
        
        w0 += l0.T.dot(l1_delta)
        w1 += l1.T.dot(l2_delta)
        w2 += l2.T.dot(l3_delta)

    print("Predictions made after training: ")
    print()
    print(l3)
    print()
    print("How good are these predictions?")
    print()
    print(np.mean(l3_error))
    print()
    print("Throughout the model")
    print()
    print(err)
    print()
    print("It took ", len(err)+1, " iterations")
    return [w0, w1, w2]


print(Y)

print(0 in Y)

#NN3_sig(X, Y, .01)
