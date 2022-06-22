# db1.py
import sqlite3

# 연결 객체를 리턴받기(일단 메모리에서 연습)
con = sqlite3.connect(":memory:")
# 커서 객체를 리턴받기
cur = con.cursor()
# 테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('Frederick','010-222-3333');")
# 검색
cur.execute("select * from PhoneBook;")

for row in cur:
    print(row)

