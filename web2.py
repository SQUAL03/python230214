# web2.py
#웹서버 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, 'html.parser')

cartoons = soup.find_all("td", class_="title")

for item in cartoons:
	title = item.find('a').text
	print(title)

# 전체주석 ctrl + /
# <td class="title">
# 				<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# 						</td>
# 				<td>