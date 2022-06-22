#정규표현식 사용
import re 

#원본 로그파일
f=open('c:\\work\\PV3.txt','rt')
#복사본
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')
#최근에 쓰는 유니코드방식으로 저장할게

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): #파일의 끝부분을 찾는 것 !=같지않다 '' 비어있다EOF
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()

