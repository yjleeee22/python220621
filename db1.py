# db1.py
import sqlite3

# 연결 객체를 리턴받기(일단 메모리에서 연습)
con = sqlite3.connect(":memory:")
# 커서 객체를 리턴받기
cur = con.cursor()
# 테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('Frederick','010-222');")
# 입력 파라메터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);",(name, phoneNumber))
# 여러건을 입력
datalist = (("tom", "010-123"),("Ann","010-452")) 
#2차원 행렬- 튜플안에 튜플 가능
cur.executemany("insert into PhoneBook values (?, ?);",datalist)

# 검색
cur.execute("select * from PhoneBook;")

# 검색 메서드 사용
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---") #바깥은 리스트, 안은 튜플
print(cur.fetchmany(2))
print("---fetchall()---") #이미 앞에 1+2건을 보여줘서 버퍼에 남은건 1건뿐
print(cur.fetchall())
cur.execute("select * from PhoneBook;") #다시 검색하면
print(cur.fetchall()) #4건 다 나옴

# for row in cur:
#     print(row[0] + " , " + row[1])

