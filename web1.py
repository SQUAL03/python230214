# web1.py
from bs4 import BeautifulSoup

#파일을 읽어오기
page = open("c:\\work\\test01.html","rt", encoding='utf-8')
#검색을 위한 객체
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

print(soup.find_all('p'))

