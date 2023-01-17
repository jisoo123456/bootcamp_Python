#tuple
a='harry',
b=('harry',)
c=()  #empty tuple
d='harry','ron'  #packing
e=('hermione')  #string
f=('harry','ron')  #packing
print(f[1])

x, y=f  #unpacking
print(y)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))