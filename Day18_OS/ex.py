# os(lin,win,un,mac,unix,code x)

# ('\\user\\username\\onedrive\\desktop\\')path
# (/users/username/desktop)


import os
import time

print(os.name)
print(os.getcwd())
print(os.path.exists('/Users/Desktop/'))
print(os.path.split('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025/Day18_OS_FileHandling/ex.py'))
print(os.path.join('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025','/Day18_OS_FileHandling/ex.py'))
print(os.path.abspath('../Day18_OS_FileHandling/ex.py'))
# print(os.path.realpath())
print(os.path.dirname('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025/Day18_OS_FileHandling/ex.py'))
print(os.path.basename('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025/Day18_OS_FileHandling/ex.py'))
print(os.path.isdir('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025/Day18_OS_FileHandling'))
print(os.getcwd())
os.chdir('/Users/pjangala/Desktop')
print(os.getcwd())
# os.mkdir('TEST')
print(os.getcwd())
# os.rename('TEST','DEMO')
# os.rmdir('DEMO')
# print(time.time())
# print(time.ctime(time.time()))

print(os.getcwd())
os.chdir('/Users/pjangala/Desktop/python')
print(os.getcwd())
ct=os.path.getctime('/Users/pjangala/Desktop/python')
mt=os.path.getmtime('/Users/pjangala/Desktop/python')
at=os.path.getatime('/Users/pjangala/Desktop/python')

print(time.ctime(ct))
print(time.ctime(mt))
print(time.ctime(at))
print(os.getcwd())
os.chdir('/Users/pjangala/Desktop')
print(os.getcwd())
os.makedirs('Grand/Parent/Child')






