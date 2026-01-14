import re
# from re import fullmatch
'''
Docstring for Day25_Adv_RegulerExpressions.ex
match
findall
split
full match
group 
span

'''
print(re.match('python','python is very easy to learn. python is a high level language'))
'''
match will find the first occuronce of the given string.
'''
print(re.findall('hi','hi there? hi i am doing fine,he is my friend hinesh'))
'''
it will go through all the available pattrens and gives us the result in a list
'''
print(re.split(' ','hi there hello worl how are you doing i am doing grate'))

print(re.fullmatch('python','python').span())

'''
quantifiers.
+ (one or more)
* (zero or more)
?(zero or one)
{n} 8charer {8}
{m,n} 
'''
print(re.fullmatch('(abc)*','abcabc'))

'''
meta char
\w(word charters)(abc)(ABC)
\W(non word charters)(!@#$%^&*)( )(0 to9)
\d(0 to 9)
\D(ab,AB,!@#$%^&)
\s(whitespaces)
\S(non white spaces)
'''

'''
[]group a-z,A-Z,0-9
^[a-z] staring the pattren
[]$ ending of the pattren
[^]
'''
print(re.fullmatch(r'[a-z]{3,10}','abcdefghijkl'))

'''
pan:ABCDE1234E
'''
pattren=r'^\w{5}\d{4}\w+$'
string='ABCDE1234E'
print(re.fullmatch(pattren,string).group())