# print(1+2)
# print(1.21+12.54)
# print('py'+'thon')

# len()


class sample:
    def display(self):
        print('welcome to python')

class sub():
    def display(self):
        print('it is easy to learn')


def show(f):
    f.display()     

s=sample()
s1=sub()
show(s1)


def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(10,20,30,40)

