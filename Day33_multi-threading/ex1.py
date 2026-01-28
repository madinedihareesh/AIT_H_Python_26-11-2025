from threading import *
from time import *

class Alphabet(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            sleep(1)

t=Alphabet()

t.start()

for i in range(65,91):
    print(i)
    sleep(1)

t.join()