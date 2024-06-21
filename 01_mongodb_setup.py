
import random
from pymongo import *  # or use * including binary BSON
from bson import *


try:
    client = MongoClient("mongodb://localhost", 27017)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client["TestDB"]
print("TestDB database is created !")

# Created or Switched to collection names: Bios
collection = db.Bios

viewer_value = random.randrange(100, 999)
print("New random viewer integer: " + str(viewer_value))

record = {
    "id": 100,
    "name": { "first": "George", "last": "Jones" }
}

# inserting the data in the database
collection.insert_one(record)

for doc in collection.find({"id" : "George"}):
    print(doc)
# close the connection to MongoDB
db.close
print("MongoDB database connection closed.")

