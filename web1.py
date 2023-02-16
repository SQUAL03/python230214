# web1.py
from bs4 import BeautifulSoup

#파일을 읽어오기
page = open("c:\\work\\test01.html","rt", encoding='utf-8')
#검색을 위한 객체
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
#<p> 전부검색: 리스트 형태로 리턴
#print(soup.find_all('p'))
#<a> 전부검색
#print(soup.find_all('a'))
# <p class="outer-text">이란 조건
#print(soup.find_all('p', class_ ="outer-text"))

#태그 내부의 문자열: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)
