import sqlite3

conn=sqlite3.connect('univ.db')
cursor=conn.cursor()

data=cursor.execute('Select * from students')

part=data.fetchall()

print(part[0][1])

cursor.close()
conn.close()
