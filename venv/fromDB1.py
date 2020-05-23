from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

num = input("랭킹을 입력해주세요 : ")

def findrank(a) :
    number = int(a)
    if number <= 10 :
        a = '0' + a
    movie = db.movies.find_one({'rank': a})
    print(a,"등 영화는",movie['title'],"입니다")

findrank(num)