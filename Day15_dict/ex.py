# d={
#     1:'one',
#     '2':'two',
#     (1,2,3,4):[1,2,3,4],
#     True:1,
#     0:False,
#     'name':'Babi',
#     'name1':'Babi'
#     }

# print(d['2'])
# print(d.get('name'))

# d={
#     1:'Ace',
#     2:'thos',
#     3:'thres'
# }

# print(d)
# d[3]='three'
# print(d)

# d[4]='four'
# print(d)

# l=[(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]

# d1=dict(l)
# print(d1)

# l1=[1,2,3]
# l2=['one','two','three']
# l3=zip(l1,l2)
# for i in l3:
#     print(i)

# l4=['red','gree','yellow']
# l5=list(enumerate(l4,start=1))
# print(l5)    

# l1=[1,2,3,4]
# l2=['one','two','three']
# d1=dict(zip(l1,l2))
# print(d1)

# l3=['red','green','yellow']
# d2=dict(enumerate(l3,start=1))
# print(d2)


# d1={1:'one',2:'two',3:'three'}
# k=d1.keys()
# for i in k:
#     print(d1[i])

# v=d1.values()
# for i in v:
#     print(i)

# it=d1.items()
# for i in it:
#     print(i)  

# d1.update({4:'four',5:'five'})
# print(d1)   


# d1.pop(4)
# print(d1)

# d1.popitem()
# print(d1)

# d1.clear()
# print(d1)

# del(d1)
# print(d1)


l1=[(1,'one'),(2,'two'),(3,'three')]

d1={y:x for x,y in l1}
print(d1)
l2=[1,2,3]
l3=['one','two','three']
d2={x:y for x,y in zip(l2,l3)}
print(d2)

d3={x:y for x,y in enumerate(l3,start=0)}
print(d3)