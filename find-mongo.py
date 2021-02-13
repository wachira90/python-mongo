from pymongo import MongoClient
from random import randint

client = MongoClient('mongodb://user:pass@192.168.4.42:27017')
db = client.business


fc1 = db.reviews.count_documents({'rating': 1})
fc2 = db.reviews.count_documents({'rating': 2})
fc3 = db.reviews.count_documents({'rating': 3})
fc4 = db.reviews.count_documents({'rating': 4})
fc5 = db.reviews.count_documents({'rating': 5})

print(fc5,fc4,fc3,fc2,fc1)
