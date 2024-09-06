from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['disaster_response']

def store_data(collection_name, data):
  collection = db[collection_name]
  if isinstance(data, list):
#IF DATA IS A LIST
    for item in data:
      collection.insert_one(item)
  else:
   
    collection.insert_one(data)