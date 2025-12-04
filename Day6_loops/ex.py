'''
name='AchieversIT'



i=0
while i<len(name):
    print(name[i])
    i+=1


i=10
while i>0:
    print(i)
    i-=1


i=0
while i<11:
    print(i)
    i+=2    
'''
i=1
while i<6:
    print('* '*i)
    i+=1    

print('-------------------')
i=5
while i>0:
    print('* '*i)
    i-=1


'''
     * (4 spaces 1 star)
    * * (3 spaces 2 star)
   * * * (2 spaces 3 star) (' '*(5-i)+'* '*i)
  * * * * (1 space 4 star)
 * * * * *(0 space 5 star)         

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
i=1
while i<6:
    print(' '*(5-i)+'*'*i)
    i+=1
