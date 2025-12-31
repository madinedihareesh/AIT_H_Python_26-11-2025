import os
import csv
import pprint
os.chdir('/Users/pjangala/Desktop/')

studict={}
with open('Stuinfo.csv','r') as f:
    data=csv.DictReader(f)
    for i in data:
        studict[i['name']]=i

# pprint.pprint(studict)

keys=studict.keys()

for i in keys:
    if i=='name3':
        print(studict[i]['email'])

l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1[0][0])        
