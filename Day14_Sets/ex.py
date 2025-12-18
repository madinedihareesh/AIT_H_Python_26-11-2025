# s={1,'hareesh',12.59,True,12.59}
# print(type(s))
# print(s)
# s1={1:'one'}
# print(type(s1))
# s2=set('python')
# print(s2)
# s3=set([1,2,3,4])
# print(s3)
# s3.add(5)
# print(s3)

s4=set()

A={1,2,3,5,7}
B={5,7,9,10,11}

c=A.union(B)
print(c)

# A=A.union(B)
# print(A). union_update

D=A.intersection(B)
print(D)

# A.intersection_update(B)
# print(A)

E=A.difference(B)
print(E)

F=A.symmetric_difference(B)
print(F)

G=A|B
print(G)

H=A&B
print(H)

I=A-B
print(I)

J=(A-B)|(B-A)
print(J)

# add
a={1,2,3,4,5,6}
a.add(7)
print(a)

a.remove(7)
print(a)

a.update([7,8,9])
print(a)

b=a.copy()
print(b)

a.pop()
print(a)


print(sum(a))
print(min(a))
print(max(a))

# a.clear()
# print(a)

# del(a)
# print(a)

b=a
print(b)