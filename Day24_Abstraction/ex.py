from abc import ABC,abstractmethod
class parent(ABC):
    def pm(self):
        print('parent method one')
    @abstractmethod    
    def pm2(self):
        pass   


class child(parent):
    def cm(self):
        print('child method 1') 
    def pm2(self):
        print('child method overriding parent abstract method')
c=child()
c.pm() 
c.cm()
c.pm2()     

print(child.mro())