from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

name=input('Enter the name of contact or group you want to text: ')
text=input('Enter the text you want to send: ')
n=int(input('Enter the number of times you want the text to be sent: '))
input('Make sure you have scanned the QR code of whatsapp web. After that, press any key')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

text_box = driver.find_element_by_class_name('_3u328')

for i in range(n):
    text_box.send_keys(text)
    butn = '_3M-N-'
    button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,butn)))
    button.click()