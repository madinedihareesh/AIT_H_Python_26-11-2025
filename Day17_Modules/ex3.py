from random import randint
print('-----Guese My number Game------')
scoure=20
rand=randint(1,10)

while scoure>0:
    num=int(input('Enter the number:'))
    if rand==num:
        print('your score is :',scoure)
        print('the random number:',rand)
        print('you won the game!')
    else:
        scoure-=4
        print('try again')
else:
    print('you lost the game')            