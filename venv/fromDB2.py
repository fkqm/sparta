from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

movie = db.movies.find_one({'title' : '매트릭스'})
s = movie['star']
name = list(db.movies.find({'star' : s}))
for m in name :
    db.movies.update_one({'title' : m['title']}, {'$set' : {'star' : 0}})
