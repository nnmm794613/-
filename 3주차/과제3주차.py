import requests
from bs4 import BeautifulSoup
import re # regular expression 라이브러리. 꼭 알 필요는 없지만 그냥 알아두자(?)


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

songs = list(soup.select('#body-content > div.newest-list > div > table > tbody > tr')) #:nth-child(1) > td.info > a.title.ellipsis'

for song in songs:
    Name = song.select_one('td.info > a.title.ellipsis')
    Rank = song.select_one('td.number')
    Singer = song.select_one('td.info > a.artist.ellipsis')
    Ost = song.select_one('td.info > a.albumtitle.ellipsis')


    if Name is not None:
        print(",".join([re.findall("\d+", Rank.text.strip())[0], Name.text.strip(), Singer.text.strip(), Ost.text.strip()]))

