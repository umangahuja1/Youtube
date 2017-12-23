from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.saavn.com/s/featured/english/Weekly_Top_Songs')

soup = BeautifulSoup(res.text, 'lxml')

data = soup.find('ol', {'class': 'content-list'})
all_songs = data.find_all('div', {'class': 'details'})

for count, s in enumerate(all_songs, 1):
    song = s.find('p', {'class': 'song-name'})
    print(count, song.text)
