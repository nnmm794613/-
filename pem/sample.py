from flask import Flask, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/update_count', methods=['POST'])
def update_count():
    sentence = request.form['sentence']
    found_sentence = db.sentences.find_one({"sentence": sentence})
    if (found_sentence is None):
        db.sentences.insert_one({text: sentence, count: 1})
    else:
        db.sentences.update_one({"sentence": sentence}, {"$set": {count: found_sentence["count"] + 1}})


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)