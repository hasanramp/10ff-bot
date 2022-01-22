from bs4 import BeautifulSoup

src = open('index.html', 'r').read()
soup = BeautifulSoup(src, 'lxml')
words = soup.find_all('span')
for word in words:
    print(word.text)