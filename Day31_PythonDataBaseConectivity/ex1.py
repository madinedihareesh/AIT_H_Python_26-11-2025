import sqlite3

conn=sqlite3.connect('univ.db')

cursor=conn.cursor()

cursor.execute('''insert into dept values
               (10,'CSE'),
               (20,'Mech'),
               (30,'EEE'),
               (40,'ECE')
''')

conn.commit()
cursor.close()
conn.close()