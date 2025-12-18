# l1=[]
# print(type(l1))
# l2=['python',12,12.59,True,12+11j]

# l3=list('python')
# print(l3)
# l4=list((1,2,3,4,5))
# print(l4)

# for i in l4:
#     print(i)
# print(len(l4))

# l5=l4[1:len(l4):1]
# print(l5)

# l6=l4[::2]
# print(l6)

# l4[2:4]=[6]
# print(l4)

# l4[9:9]=[10]
# print(l4)

# l4[1:1]=[12]
# print(l4)

# l1=[1,2,3,4,5]
# l2=[1,2,3,4,10]
# l3=l1+l2
# print(l3)

# l4=l1*3
# print(l4)

# print(l1<l2)

# Adding elements into the list
L1=[1,2,3,4,5]
# append
L1.append(6)
print(L1)
L1.extend([7,8,9])
print(L1)

L1.insert(1,10)
print(L1)

L2=L1.copy()
print(L2)

# removing elemnts from the list
L2.pop(1)
print(L2)
# remove
L2.remove(9)
print(L2)

L2.clear()
print(L2)

del(L2)

L1.append(10)
print(L1)
print(L1.index(10,L1.index(10)+1))

L1.reverse()
print(L1)

L1.sort()
print(L1)

# List comprohension
L4=[i**2 for i in range(1,6)]
print(L4)

Nl=[[1,2,3],[4,5,6],[7,8,9]]
print(Nl[0][0])

for i in range(0,3):
    for j in range(0,3):
        print(Nl[i][j],end=' ')
    print('')    