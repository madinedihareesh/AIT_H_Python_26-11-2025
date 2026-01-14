class Sample:
    name='Abhi'
    age=20
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    @staticmethod    
    def demo(l,b):
        print(2*l*b)    


# ___sizeof__()
# single inheritance
'''
class praent:
    def display(self):
        print('Hello son')
class child(praent):
    def show(self):
        print('Hello father') 

child().show()
child().display()              
'''

class grandfather:
    def gf(self):
        print('Grandfather')
class parent(grandfather):
    def p(self):
        print('Parent')
class child(parent):
    def c(self):
        print('child')

child().gf()                        



   