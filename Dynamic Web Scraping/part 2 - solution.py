from bs4 import BeautifulSoup
from selenium import webdriver

##------------------------ changes in this part only --------------------------------- ##

driver = webdriver.Chrome()
driver.get('https://www.hackerearth.com/challenges/')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res, 'lxml')

##------------------------ changes end here. Rest of the things are same. ------------------ ##

box = soup.find('div', {'class': 'upcoming challenge-list'})

all_hackathons = box.find_all('div', {'class': 'challenge-card-modern'})

for hackathon in all_hackathons:
    h_type = hackathon.find('div', {'class': 'challenge-type'}).text.replace('\n', '')
    name = hackathon.find('div', {'class': 'challenge-name'}).text.replace('\n', '')
    date = hackathon.find('div', {'class': 'date'}).text.replace('\n', '')

    print(h_type, name, date)
