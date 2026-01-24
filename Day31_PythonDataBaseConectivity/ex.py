import sqlite3

conn=sqlite3.connect('univ.db')

cursor=conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON')

cursor.execute('create table dept(' \
'deptno integer primary key,' \
'dname text)')

cursor.execute('create table students(' \
'roll integer primary key,' \
'name text,' \
'loc text,' \
'deptno integer,' \
'foreign key(deptno)' \
'references dept(deptno))')

conn.commit()

cursor.close()
conn.close()