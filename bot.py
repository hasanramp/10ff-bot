from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get('https://10ff.net')
time.sleep(3)

# Entering username
username_input = browser.find_element_by_xpath('//*[@id="username"]')
username_input.send_keys("oxide")
time.sleep(0.2)

#Clicking enter button
browser.find_element_by_xpath('/html/body/div/form/input[2]').click()
time.sleep(15)

# getting words input field
#/html/body/div/div/div[3]/div[2]/div[1]/div
to_read_words = browser.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[1]/div')
words_input_field = browser.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/input')
src = to_read_words.get_attribute('innerHTML')
soup = BeautifulSoup(src, 'lxml')
words = soup.find_all('span')
for word in words:
    to_put_word = word.text
    words_input_field.send_keys(to_put_word + ' ')