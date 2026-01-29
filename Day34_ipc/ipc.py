from threading import *
from time import *

class Mydata:
    def __init__(self):
        self.data=0
        self.flag=False
        self.lock=Lock()

    def put(self,d):
        while self.flag !=False:
            pass
        self.lock.acquire()
        self.data=d
        self.flag=True
        self.lock.release()

    def get(self):
        while self.flag !=True:
            pass
        self.lock.acquire()
        x=self.data
        self.flag=False
        self.lock.release()
        return x

def producer(data):
    i=0
    while True:
        data.put(i)
        print('producer:',i)
        i+=1
        sleep(1)


def consumer(data):
    while True:
        x=data.get()
        print('consumer:',x)
        sleep(1)

data=Mydata()

t1=Thread(target=lambda:producer(data))
t2=Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()