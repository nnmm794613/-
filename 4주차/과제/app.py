from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/products', methods=['POST'])
def test_post():
    name_receive = request.form['name']
    count_receive = request.form['count']
    address_receive = request.form['address']
    phone_receive = request.form['phone']

    print(name_receive)
    print(count_receive)
    print(address_receive)
    print(phone_receive)

    db.products.insert_one({
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    })

    return jsonify({'result':'success', 'msg':'이 요청은 POST'})

@app.route('/products', methods=['GET'])
def test_get():
    products = list(db.products.find({},{'_id': 0}))
    print(products)
    return jsonify({'result':'success','products':products})

if __name__ == '__main__':
    app.run('localhost',port=5000,debug=True)
