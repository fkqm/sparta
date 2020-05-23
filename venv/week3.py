import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songlist = soup.select('#body-content > div > div > table > tbody > tr.list')
for song in songlist:
    rank = song.select_one('td.number')
    songrank = rank.text[0:2]
    a_tag = song.select_one('td.info > a')
    songtitle = a_tag.text
    a_singer = song.select_one('td.info > a.artist.ellipsis')
    singer = a_singer.text
    print (songrank.strip(), songtitle.strip(), singer)