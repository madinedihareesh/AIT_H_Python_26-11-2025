User=input('Enter the Name:')
Password=input('Enter the password')
Bal=int(input('Enter the first diposite amount:'))
print('Enter username and Password')
username=input('Enter the user name')
cpassword=input('Enter the password')
if User==username and Password==cpassword:
    while True:
        print('1.Withdrawl')
        print('2.Dipoite')
        print('3.Check bal')
        print('4.Logout')
        opction=int(input('Enter you choice'))
        if opction==1:
            withdrawlamt=int(input('Enter the amount to withdraw'))
            if Bal>withdrawlamt:
                Bal=Bal-withdrawlamt
                print(withdrawlamt,'is debited from your acount and current bal is',Bal)
            else:
                print('Insufficient funds')    
        if opction==2:
            dipositeamt=int(input('Enter the amount to be diposited:'))
            if  dipositeamt>0:
                Bal=Bal+dipositeamt
                print('Diposited successful your current bal is',Bal)    
            else:
                print('The amount has to be grater than 0') 
        if opction==3:
            print(Bal)
        if opction==4:
            break    
else:
    print('Enter Valid Username and password')                      