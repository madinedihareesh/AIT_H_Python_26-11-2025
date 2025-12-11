# sum of n natural number
'''
n=int(input('Enter a number'))
i=1
s=0
while i<=n:
    s+=i
    i+=1
print(s)  
'''
# even numbers from 1 to 100:
'''
i=0
while i<=100:
    if i%2==0:
        print(i,'is a even number')
    i+=1    
'''
#find the factors of a given number:
'''
n=int(input('Enter the number'))
i=1
while i<=n:
    if n%i==0:
        print(i,'is a factor of',n)
    i+=1 
'''

# find the given number is a prime or not
'''
n=int(input('Enter a number'))
i=1
count=0
while i<=n:
    if n%1==0:
        count+=1
    i+=1
if count==2:
    print(n,'is a prime number')
else:
    print(n,'is not a prime number') 
'''

# fobbanoci:
'''
0 1 1 2 3 5 8

n=int(input('Enter a number'))
i=1
a=0
b=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1
'''
'''
i=1
while i<101:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,'is aprime number')
    i+=1            
'''
name='AchieversIT'
vovels='aeiouAEIOU'
i=0
while i<len(name):
    if name[i] in vovels:
        print('*')
    else:
        print(name[i]) 
    i+=1       

'''
1. Analyze the problem
2. Bulid the logic for the problem
3. Breakdown the logic 
4. Bulid the logic pecies
5. COmbine the peices
'''