'''
class parent:
    def __init__(self):
         print('Hello')

    def display(self):
        print('THis is  a parent class')

class Child(parent):
    def __init__(self):
        super().__init__()  

    def show(self):
        print('This is a clid class')
'''
# c=Child()

# instance>>class>>inherited class>>constructer

# c=Child()
# c.display()

# class nameofclass:
#     def __init__(self):
#         pass
#     def add(self,a,b):
#         print(a+b) 

# n=nameofclass()     
# n.add(10,20)   
'''
class greandparent:
    def gf(self):
        print('He is the Head of the family')

class parent(greandparent):
    def p(self):
        print('He is earning')

class child(parent):
    def c(self):
        print('He is studing')

p=parent()
p.p()
p.gf()                          
'''
'''
class Nag:
    def skill(self):
        print('He is a Business man')

class chaitu(Nag):
    def pro(self):
        print('in collection of cars')

class akhil(Nag):
    def dancer(self):
        print('he is a dancer')


c=chaitu()
c.pro()
c.skill()   

a=akhil()
a.dancer()
a.skill()
'''

'''
class father:
    def skill(self):
        print('He is a business man')

class mother:
    def teach(self):
        print('She is a teacher')

class son(father,mother):
    def dance(self):
        print('He is a good dancer')

s=son()
s.dance()
s.skill()
s.teach()
'''
'''
class A:
    def a(self):
        print('IT is class \'A\'')
class B(A):
    def b(self):
        print('It is class \'B\'')  
class C(B):
    def c(self):
        print('ift is class\'C\'')
class D(C,B):
    def d(self):
        print('It is class \'D\'')

d=D()
d.a()
d.b()
d.c()
d.d()                            
'''


class Example:
    def __init__(self,l,h):
        self.a=l
        self.b=h
    def area(self):
        print(self.a*self.b)
    @staticmethod    
    def diff(self):
        print('This is defining the static method')

e=Example(10,5)
e.area()
e.diff()
