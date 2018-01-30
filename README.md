# Tweet Monitor

## Prerequisites

#### Without Docker

* download mongodb

* run:

         sudo service mongod start

* install the pip requirements

   	   pip install -r requirements.txt

* Create a file keys.txt with your twitter keys

* run:

         python3 pymongo_tweepy.py


#### With Docker

* install docker

* create a file keys.txt with your twitter keys

* delete the .dockerignore file so that your keys.txt are copied into the container

* run:

         docker build -t tweet-mongo:latest .

* Once this completes, run

         docker run -itd --name=tweet-mongoc tweet-mongo

* Check that the container is running, using:

         docker container ls

* Run:

         docker exec -it tweet-mongoc /bin/bash

* within the container, you can now run

         python3 pymongo_tweepy.py


## Follow along with jupyter

[Here](./Collection-And-Analysis-Of-Tweets.ipynb) you will find a walk through of the analysis.
