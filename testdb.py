import sqlite3
conn = sqlite3.connect('mydb.db')

# Cursor 객체 생성
c = conn.cursor()

# 학번을 검색해서 정보 출력
num = ('20201234' ,)
c.execute('SELECT * FROM student WHERE num  =?', num)
print(c.fetchone())

# 접속한 db 닫기
conn.close()


#CREATE TABLE "users" (
#	"id"	varchar(50),
#	"pw"	varchar(50),
#	"name"	varchar(50),
#	PRIMARY KEY("id")
#)