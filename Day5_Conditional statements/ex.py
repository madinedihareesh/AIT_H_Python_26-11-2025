'''
1. If condition (simple if)
2. if else
3. elif lader
4. nested conditonal statements
5. terinary
6. match
'''
'''
if condition:
    statement
'''

username='John'
password='Welcome@123'


print(2+3==5)

if 2+3==5 or 3-2==2:
    print('THis is a valid user')


'''
if condition:
     block of code (statement)
else:
    block of code (statement)     
'''  

bal=0

if bal>0:
    print('you can withdraw the amount')
else:
    print('you account bal is zero') 

'''
if condtion:
    block
elif condition:
    block
elif condition:
    block
else:
    block        

''' 
meansoftransport='nothing' 

if meansoftransport=='Bus':
    print('I am travaling by bus')
elif meansoftransport=='train':
    print('I am travaling by train')
elif meansoftransport=='car':
    print('i am travaling by car')
elif meansoftransport=='bike':
    print('i am travaling by bike')  
else:
    print('i have droped my plans')  


flavor=input('Enter you flavor name:')

if flavor=='vanila':
    print(flavor,'is Available,how many scoops you required')
elif flavor=='Redvelwet':
    print(flavor,'is Available,how many scoops you required')
elif flavor=='choclet':
    print(flavor,'is Available,how many scoops you required')
else:
    print(flavor,'is not available')     



'''
if condtion:
    if condtion:
        block
    else:
        block
else:
    block            
'''

bill=int(input('Enter you bill amount:'))

if bill>1000:
    if bill>=10000:
        dis=bill*0.25
        print('toal discounted price',(bill-dis))
    elif bill>=5000 and bill<10000:
        dis=bill*0.15
        print('toal discounted price',(bill-dis))  
    elif bill>=3000 and bill<5000:
        dis=bill*0.1
        print('toal discounted price',(bill-dis)) 
    elif bill>1000 and bill<3000:
        dis=bill*0.05
        print('toal discounted price',(bill-dis))
    else:
        print('No discont for ₹1000')     
else:
    print('You are not elisible for discount',bill)  

'''
value_if_true if condition else 'false_value'
'''

age=25
res='Adult' if age>18 else 'minor'
print(res)

'''
conditon

match conditon:
    case 1:
        statement
    case 2:
        statement
    case 3:
        statement
    case 4:
        statement            
'''
day=int(input('enter day no:'))

match day:
    case 1:
        print('Sunday')
    case 2:
        print('Mon')
    case 3:
        print('Tus')
    case 4:
        print('wed')
    case 5:
        print('Thurs')
    case 6:
        print('Fri')
    case 7:
        print('Sat')                        