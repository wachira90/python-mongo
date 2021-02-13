from pymongo import MongoClient

#include pprint for readabillity of the 
from pprint import pprint
#change the MongoClient connection string to your MongoDB database instance

client = MongoClient('mongodb://user:pass@192.168.4.42:27017')
# client = MongoClient(port=27020)
db=client.business
ASingleReview = db.reviews.find_one({})

print('A sample document:')
pprint(ASingleReview)
result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))
UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)

'''
A sample document:
{'_id': ObjectId('5f04209cf0a3c5fdfd281231'),
 'cuisine': 'American',
 'name': 'Salty Kitchen Inc',
 'rating': 4}
Number of documents modified : 1
The updated document:
{'_id': ObjectId('5f04209cf0a3c5fdfd281231'),
 'cuisine': 'American',
 'likes': 1,
 'name': 'Salty Kitchen Inc',
 'rating': 4}
 '''