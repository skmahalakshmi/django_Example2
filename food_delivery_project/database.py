# connect to sqlite3
import sqlite3

db = sqlite3.connect('Registration')
# created cursor from database registration
rs = db.cursor()
rs.execute('''create table register(name varchar(50),email varchar(100),phone varchar2(10),passwd varchar(10))''')

rs.execute(''' insert into register values('kaha','@gmail.com','1234567890','maha') ''')
db.commit()
data=[]
k=rs.execute('select * from register')
for i in k:
    data.append(i)
    print(i)

