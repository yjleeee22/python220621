# DemoForm2.py
# DemoForm2.ui(디자인) + DemoForm2.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹 크롤링
import urllib.request
from bs4 import BeautifulSoup

# 디자인 파일 로딩 
# 슬라이싱 하는 이유 - ui파일이 하나가 아닐수 있어서
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #생성자 메서드 --- 다중상속
    def __init__(self):
        super().__init__() #초기화 메서드 양쪽에 잇는 걸 다 불러옴
        self.setupUi(self)
    #슬롯 메서드 정의
    def firstClick(self):
        # 파일로 저장
        f = open("c:\\work\\webtoon.txt", 'wt', encoding="utf-8")
        # 동적으로 주소 생성
        for i in range(1,6):
            #  웹페이지의 실행결과를 문자열로 받기 폴더명(.파일명).함수명
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            # 검색을 할 객체 생성
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text
                print(title.strip())
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText("네이버 웹툰 크롤링 종료~~")
    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼클릭~~")

# 진입점 체크
if __name__ == "__main__":
    #실행 프로세스
    app = QApplication(sys.argv)
    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show()
    #이벤트 처리 대기
    app.exec()