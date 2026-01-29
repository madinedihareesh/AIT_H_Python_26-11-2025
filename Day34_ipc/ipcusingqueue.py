from threading import *
from time import *
from queue import *



def producer(q):
    i=0
    while True:
        q.put(i)
        print('producer:',i)
        i+=1
        sleep(1)


def consumer(q):
    while True:
        x=q.get()
        print('consumer:',x)
        sleep(1)

q=Queue()

t1=Thread(target=lambda:producer(q))
t2=Thread(target=lambda:consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()