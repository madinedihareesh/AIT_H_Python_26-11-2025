import sqlite3

conn=sqlite3.connect('univ.db')
cursor=conn.cursor()

for i in range(1,16):
    roll=int(input('Enter student roll number:'))
    name=input('Enter name of the student:')
    loc=input('Enter loc of the student:')
    deptno=int(input('Enter the deptno of student:'))

    cursor.execute(f'''insert into students values
                   ({roll},'{name}','{loc}',{deptno})
''')
    
    conn.commit()

cursor.close()
conn.close()

