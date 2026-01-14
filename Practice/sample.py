'''
Docstring for Practice.sample
def name(arguments1,arg2):
     block
'''
'''
def sample():
    return 'Hello world'


print(sample())


def add(a=0,b=0):
    sum=a+b
    return sum

print(add(10,20))
'''
'''
def sum(a,b,/,*,c,d):
    sum=a+b+c+d
    return sum

print(sum(10,20,c=30,d=40))
'''
'''
def sum(**args):
    for i in args:
        print(args[i])
    
sum(a=10,b=20,c=30)
'''

'''
def outter(a,b):
    def inner():
        print(a+b)
    inner()

outter(10,20)
'''
'''
def sample():
    print('Hello world')

def sample1(a):
    a()

sample1(sample)    
'''
'''
def deco(f):
    def wrp():
        print('hello')
        f()
        print('hello')
    return wrp

@deco
def sample():
    print('world')


sample()    
'''

'''
def sum(a,b,c,d):
    return a+b+c+d
x=sum(30,40,50,60)
print(type(x))
def total(a,b,f):
    print(a+b+f)

total(10,20,x) 
'''
'''
class sample:
    age=20
    def __init__(self,name):
        self.name=name

    def depen(self):
        print(self.name) 
    @staticmethod
    def nondep():
        print('hello world')  
print(sample.age)
sample('babi').depen()     


i=1
while i<6:
    print('*'*i)
    i+=1

for i in range(1,6):
    print('*'*i)   

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='') 
    print()    
'''
'''
_ _ * _ _
_ * _ * __
_ * * * _
_* * * *
* * * * *
'''

for i in range(1,6):
    print(' '*(5-i)+'* '*i)
    



   

      




  