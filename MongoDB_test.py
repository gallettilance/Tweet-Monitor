from pymongo import MongoClient
from pprint import pprint
client = MongoClient("localhost", 27017)
print(client)
MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
db=client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
