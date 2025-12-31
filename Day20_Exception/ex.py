'''
try:
  condtion
except typeof exceptions:
   statemnt
else:
    exigutable code
finally:
    statement         
'''
a=input('Enter a number')
b=input('Enter B number')

try:
    c=int(a)
    d=int(b)
    c//d
except Exception as msg:
    print(msg)
else:
    print('sum of a and b',c//d)
finally:
    print('Program completed')                  