import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://namu.wiki/RecentChanges',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

keywords = soup.select('#app > div > div > article > div > table > tbody >tr > td ')
for keyword in keywords:
    # movie 안에 a 가 있으면,
    a_tag = keyword.select_one('div.v-popover > div > a')
    if a_tag is not None:
        # a의 text를 찍어본다.
        print (a_tag.text)