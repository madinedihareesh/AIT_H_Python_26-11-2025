# t=(12,12.59,True,[1,2,3],'Achievers',12+11j,12)
# print(t)
# t[0]=13
# t[0:0]=14


# t1=(1,2,3,4)
# t2=(5,6,7,8)
# t3=t1+t2
# print(t3)

# t4=t1*3
# print(t4)

# t1=tuple([1,2,3,4,5,6])
# t2=t1[::-1]
# print(type(t2))

# t3=t1[1:6:1]
# print(t3)

t1=10,20,30,40,50,10
print(t1)

a,b,*c=t1
print(c)

print(t1.count(10))

# (exp for item in sequnce)

t2=(*(x for x in range(1,11)),)
print(t2)

t3=tuple([x for x in range(1,11)])










