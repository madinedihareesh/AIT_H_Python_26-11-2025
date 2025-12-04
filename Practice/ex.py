year=int(input('Enter the Year:'))

if year%100==0:
    if year%400==0:
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
elif year%4==0:
    print(year,'leap year')
else:
    print(year,'is not a leap year')       


vovels='aeiouAEIOU'

char=input('Enter any char with in alpha:')

if char in vovels:
    print('It is a vovel')
else:
    print('It is a constaint')    
    