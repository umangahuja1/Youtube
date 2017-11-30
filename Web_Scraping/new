from bs4 import BeautifulSoup
import requests

res = requests.get('http://indiatoday.intoday.in/section/120/1/top-stories.html')
soup = BeautifulSoup(res.text, 'lxml')

news_box = soup.find('ul', {'class': 'topstr-list gap topmarging'})
all_news = news_box.find_all('a')

for news in all_news:
    print(news.text)
    print()
