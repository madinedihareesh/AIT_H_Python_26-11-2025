'''
Docstring for Day23_Encaps.ex
Access Spacifiers:
1.Public
2.protected
3.private
'''

'''
class Sample:
    def __init__(self,a):
        self.__a=a
    def display(self):
        print(self.__a)
s=Sample(10)
s._Sample__a=20

s.display()
class sub(Sample):
    def show(self):
        print(self.__a)
'''

# inner class:

class outer:
    def __init__(self):
        self.nest=self.inner()

    def show(self):
        print('HI,')
        self.nest.display()    
    class inner:
        def display(self):
            print('Hello world')

outer().show()            
