import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.macmillandictionary.com/dictionary/british/castle',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.   <span class="SEPPRON-before"> /</span>ˈwɔːtə(r)<span class="SEPPRON-after">/</span></span>'
soup = BeautifulSoup(data.text, 'html.parser')

words = soup.select('#entryContent > div > div.col-xs-12.col-sm-8.col-md-content-with-right.left-content > div.middle-xs.entry-pron-head.row.no-margin > div.PRONS.dflex.no-grow.middle-xs > span.PRON')

for word in words: 
    title = word.select_one(ˈ
print(words)