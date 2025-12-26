# function--resuable block of code.
# uses of function
# 1.resuablity(avoids repeting the code)
# 2.making a big promgram into small pecies
# 3.code optimization

# print()
# id()
# dir()
# type()
# len()
# max()
# sum()
# input()

# user defined functioin

# syntax:

# def functionname(arrguments):
#     statemsts/block of code
#     return statemts
'''
# basic function:
def greet():
    print('hello world!')

greet()

# functions with arguments:

def even(number):
    if number%2==0:
        print('even')
    else:
        print('odd')   


even(10)  


# function with return statement.

def add(number,number1):
    return number+number1

print(add(1,2))

# functions with multiple return statements.
def maths(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return f'addition:{add},sub:{sub},mul:{mul}'

print(maths(10,5))


# function with default arguments:
def area(l,b,h=30):
    print(l*b*h)

area(10,20,15)    


# two types arrguments:
# postional arguments
# keyword arguments

def sample(a,b,c):
    print(f'a:{a},b:{b},c:{c}')

sample(c=30,a=20,b=10)   

# positional only arguments
def pos(a,b,c,/):
    print(a,b,c)

pos(20,30,10)

# keyword only arguments:
def ke(*,a,b,c):
    print(a,b,c)

ke(b=1,c=2,a=3) 


# mixed postional and keyword arggument

def sample1(a,b,c,d,/,*,e,f,g,h):
    print(a,b,c,d,e,f,g,h)

sample1(1,2,3,4,e=5,f=6,g=7,h=8) 
'''

# variable length postiional arguments
'''
def add(*args):
     sum=0
     for i in args:
          sum+=i
     return sum

print(add(1,2,3))     
'''

# variable length keyword arguments:
'''
def sample(**kwargs):
    d=kwargs
    return d

print(sample(a=10,b=20,c=30))  
'''

# nested functions:
'''
def outter():
    def inner():
        print('inner function')
    print('outter function')    
    inner()
        
    
outter()  

# first class object:

show=print
show('Hello world')   
'''

# call back function/higher order function
'''
def squre(n):
    return n*n


def cube(a,n):
    return n*a(n)

print(cube(squre,3))
'''

# decarator functions
'''
def my_decorator(func):
    def wrapper():
        print('Before function')
        func()
        print('After function')
    return wrapper

@my_decorator
def show_def():
    print('hello')

show_def()    
'''

# lamida functions:

# add=lambda x: x**2

# print(add(10))


# function with multiple return statements
'''
def math(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
   


print(math(10,5))
'''

# clousers(the inner function has the ebility to read the outter function variables/paramets)
'''
def outter():
    name='AchieversIT'
    def inner():
        print(f'welcome{name}')
    inner()
    def inner2():
        print(f'welcome{name}')
    inner2()    

outter()  
'''
'''
def outter(a,b):
    def inner():
        sum=a+b
        print(sum)
    inner()

outter(10,5)  
'''

# lambda (condtion):'Acc','rej'
'''
pro='Harddisk'
space=32
price=19.12

# %s=string,%d=digit,%g=float,%f=float,%F=float,%i=integer

print('the price of %d GB %s is %g'%(space,pro,price))

print('the price of {1} GB {0} is {2}'.format(pro,space,price))

print(f'the price of {space} gb {pro} is {price}')

samplie('Abhi')

def samplie(name):
    print(f'welcome {name}')
'''

def decorator(f):
    def wrapper():
        print('befour function')
        f()
        print('after fucntion')
    return wrapper    

@decorator
def greet():
    print('welcome')  


greet() 

@decorator
def sample():
    print('Hello world')

sample()    


