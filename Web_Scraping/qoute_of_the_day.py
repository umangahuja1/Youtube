from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.brainyquote.com/quote_of_the_day')
soup = BeautifulSoup(res.text, 'lxml')

image_quote = soup.find('img', {'class': ' p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
print(image_quote['alt'])
