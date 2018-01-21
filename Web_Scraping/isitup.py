from bs4 import BeautifulSoup
import requests

url = input('Enter the url : (duckduckgo.com) : ')

res = requests.get('https://isitup.org/' + url)

soup = BeautifulSoup(res.text, 'lxml')

out_box = soup.find('div', {'id': 'container'})
result = out_box.find('p').text

print(result)
