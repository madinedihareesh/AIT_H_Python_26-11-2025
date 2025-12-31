import os

os.chdir('/Users/pjangala/Desktop')

os.chdir('/Users/pjangala/Desktop/AIT_H_Python_26-11-2025/Day19_FileHandling')
# f=open('sample.txt','r')
# print(f.read())
'''
f=open('Sample.txt','w')
f.write('''
'''
Hi hello how are you,
i am doing grate
now i am learning python  
'''              
''')
f.close()

with open('Sample.txt','r') as fa:
    text=fa.read()
print(text)
'''
'''
f=open('Sample.txt','w')
f.write('''
'''
it is very easy to learn
i am very happy in learning python 
'''        
''')
f.close()
'''
'''
with open('Sample.txt','r+') as f:
    text=f.read()
    
    f.writelines('''
'''
Hi hello how are you
'''
''')
print(text)
'''

f1=open('images.png','rb')
img=f1.read()

f1.close()

f2=open('image.png','wb')
f2.write(img)
f2.close