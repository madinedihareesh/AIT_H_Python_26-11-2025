from threading import *
from time import *


def display(str):
    l.acquire()
    for x in str:
        print(x)
        sleep(1)
    l.release()

l=Semaphore(2)
t=Thread(target=display,args=('HELLO WORLD',))
t1=Thread(target=display,args=('you are welcome',))
t2=Thread(target=display,args=('0123456789',))

t.start()
t1.start()
t2.start()

t.stop()
t1.stop()
t2.stop()

