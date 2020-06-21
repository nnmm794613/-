import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      

app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

# @app.route('/update_count', methods=['POST'])
# def update_count():
#     sentence = request.form['sentence']
#     found_sentence = db.sentences.find_one({"sentence": sentence})
#     if (found_sentence is None):
#         db.sentences.insert_one({text: sentence, count: 1})
#     else:
#         db.sentences.update_one({"sentence": sentence}, {"$set": {count: found_sentence["count"] + 1}})

def get_phonetics(search_text):
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.macmillandictionary.com/dictionary/british/' + search_text,headers=headers)

    
    soup = BeautifulSoup(data.text, 'html.parser')

    word = soup.select_one('#entryContent > div > div.col-xs-12.col-sm-8.col-md-content-with-right.left-content > div.middle-xs.entry-pron-head.row.no-margin > div.PRONS.dflex.no-grow.middle-xs > span.PRON', text=True)

    return word.text

@app.route('/phonetics')
def phonetics_get():
    search_text = request.args.get('search_text')
    phonetics = get_phonetics(search_text)
    return jsonify({'result': 'success', 'phonetics': phonetics})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
