# web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#웹페이지 로딩
page = open("c:\\work\\test01.html","rt", encoding="utf-8").read()

# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

# 문서를 그대로 보기
# print(soup.prettify())

# <p>태그 전체를 검색
# print(soup.find_all("p"))

# 첫번째 <p> 검색
# print(soup.find('p'))

# 조건이 있는 경우:<p class=outer-text> 
# class랑 구분하기 위해 "class_" 사용
# print(soup.find_all("p", class_="outer-text"))

# #id 속성으로 검색
# print(soup.find_all(id="first"))

#문자열만 리턴
# .text <-앞뒤 태그를 없애고 텍스트만 가져옴 / .replace 빈줄 없앰
for item in soup.find_all("p"):
    title = item.text
    title = title.replace("\n","")
    print(title.strip())


