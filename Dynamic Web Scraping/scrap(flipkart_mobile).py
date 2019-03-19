import requests
from bs4 import BeautifulSoup

n1 = []
x = int(input("Enter page number you want to scrap = "))
for i in range(1,x+1):
    n1.append(i)

for page in n1:
    print("######################################################################################")

    b_url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_4&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4&as-pos=0&as-type=RECENT&as-backfill=on&page="
    url = b_url + str(n1[page-1])

    sc = requests.get(url)
    soup = BeautifulSoup(sc.text, 'html.parser')

    phone = soup.findAll('div',{'class':'_3wU53n'})
    prize = soup.findAll('div',{'class':'_1vC4OE _2rQ-NK'})

    count = 0

    for name in phone:
        print(phone[count].text)
        print(prize[count].text)
        count += 1
