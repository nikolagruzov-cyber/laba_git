a=20
b=20
a1=int(input())
b1=int(input())
a2=’20’
b2=str(20)

print(a==b)
print(a1==b1)
print(a2==b2)

print(a is b)
print(a1 is b1)
print(a2 is b2)

print(id(a), id(b), id(a1), id(b1), id(a2), id(b2))

n=None
print(n==None, n is None)
