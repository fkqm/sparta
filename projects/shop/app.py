from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/shop', methods=['GET'])
def listing():
    purchases = list(db.purchases.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'purchases': purchases})

# API 역할을 하는 부분


@app.route('/shop', methods=['POST'])
def buying():
    # 1. 클라이언트로부터 데이터를 받기
    username_receive = request.form['username_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    purchase = {
        'username' : username_receive,
        'quantity' : quantity_receive,
        'address' : address_receive,
        'phone' : phone_receive,
        }

    # 3. mongoDB에 데이터 넣기
    db.purchases.insert_one(purchase)
    return jsonify({'result': 'success', 'msg': '주문이 정상처리 되었습니다.'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
