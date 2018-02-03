# Problem with normal web scraping and need of dynamic scraping

## this will not give any output. It is just to explain the need of dynamic scraping

from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.hackerearth.com/challenges/')
soup = BeautifulSoup(res.text, 'lxml')

box = soup.find('div', {'class': 'upcoming challenge-list'})

all_hackathons = box.find_all('div', {'class': 'challenge-card-modern'})

for hackathon in all_hackathons:
    h_type = hackathon.find('div', {'class': 'challenge-type'})
    name = hackathon.find('div', {'class': 'challenge-name'})
    date = hackathon.find('div', {'class': 'data'})

    print(h_type, name, date)
