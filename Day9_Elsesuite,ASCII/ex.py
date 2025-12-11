# i=1
# while i<11:
#     print(i)
#     i+=1
# print('Loop ended')   


# for i in range(1,11):
#     print(i)  
# print('For loop completed')    

# for i in range(1,11):
#     if i>=1 and i<=5:
#         pass
#     else:
#         print(i)
# print('loop completed')

# for i in range(1,7):
#     if i==1:
#         pass
#     if i==2:
#         pass
#     if i==3:
#         print(i)
#     if i==4:
#         break
#         continue
#     if i==5:
#         print(i)
#     if i==6:
        
#         print('loop braking')
#         continue
#         print('loop boken')        
# print('loop completed')  

for i in range(1,11):
    if i%3==0:
        print('it is a multiple of 3')
        break
        print('it is going to continue to next loop')
    else:
        print(i)      
