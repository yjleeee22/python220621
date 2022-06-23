# coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) : 웹브라우저마다 고유한 헤더 
# ->헤더가 비어있는지만 체크하므로 적당한 값 채워넣으면 ㅇㅋ(웹봇차단)
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩 - 사기업들이 만든사이트는 대부분 깨짐
        page = data.decode('utf-8', 'ignore') #약간 깨져도 무시할게
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'}) #attrs-속성들을 지정

# <span class="subject_fixed" data-role="list-title-text">
# 	아이패드 프로 10.5인치 256기가 와이파이 (전투형, 화이트스팟)
# </span>



        for item in list:
                try:
                        title = item.text
                        # print(title.strip())
                        if (re.search('맥북', title)):
                                print(title.strip())
                except:
                        pass
        
