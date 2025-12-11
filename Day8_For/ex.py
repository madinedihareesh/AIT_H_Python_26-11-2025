'''
range(stop) starting=0,step=1
range(start,stop) step=1
range(stat,stop,step)
'''
'''
for element in sequence:
    print(element)

i=0
while i<6:
    print(i)    
'''
# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)  

# for i in range(2,21,2):
#     print(i)  

# value=int(input('Enter the number:'))
# for i in range(1,11,1):
#     print(value,'*',i,'=',value*i)


# s=input('Enter a string to verify the string is a plendrome or not:')
# rev=''
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# if s==rev:
#     print(s,'is a palendrome') 
# else:
#     print(s,'is not a plaendrome') 

# i=0
# sum=0
# while i<11:
#     sum+=i
#     i+=1
# print(sum)           

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)  
'''
*
* *
* * *
* * * *
* * * * *
'''  

# i=1

# while i<6:
#     j=1
#     while j<=i:
#         print('*',end=' ')
#         j+=1
#     print('')    
#     i+=1   

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

# for i in range(1,6):
#     for j in range(1,6):
#         if j>=i:
#          print('*',end=' ')
#     print('')    

# for i in range(1,6):
#     print(' '*(5-i),'* '*i )

num=1
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(num,end=' ')
            num+=1
    print('')        