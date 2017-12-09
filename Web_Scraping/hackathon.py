from bs4 import BeautifulSoup
import requests

res = requests.get('http://www.hackathon.io/events')
soup = BeautifulSoup(res.text, 'lxml')

all_hacks = soup.find_all('div', {'class': 'event-teaser'})

for i, hack in enumerate(all_hacks, 1):
    time = hack.find('div', {'class': 'two columns time'}).text.replace('\n', '').strip()
    name = hack.find('h4').text.replace('\n', '').strip()
    description = hack.find('h5').text.replace('\n', '').strip()
    location = hack.find('div', {'class': 'two columns location'}).text.replace('\n', '').strip()

    print("{}. {}\n{}\n{}\n{}\n\n".format(str(i), name, description, time, location))
