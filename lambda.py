from functools import reduce
x=lambda a,d:a/d
print(x(4,2))
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(4)
print(mydoubler(10))
mylist=[3,4,5,6,7,8,9]
mylist1=[3,4,5,6,7,8,9]
a=map(lambda x: x*3,mylist)
print(list(a))
b=map(lambda x,y:x*y,mylist,mylist1)
print(list(b))
c=filter(lambda x,:x%2==0,mylist)
print(list(c))
d=filter(lambda x,: True if x>=10 else False,mylist)
print(list(d))
e= reduce (lambda x,y:x+y,mylist1)
print(e)
