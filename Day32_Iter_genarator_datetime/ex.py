l1='Python'

def myrange(n):
    i=0
    while i<n:
        yield i
        i+=1
m=myrange(4) 
print(next(m))       
print(next(m)) 
print(next(m)) 
print(next(m)) 
      





