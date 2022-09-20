def gen():
    yield "a"
    yield "b"
x=gen()
print(next(x)) 
def listiterator(list):
    for i in list:
        yield i
a=[1,2,3,4,5,6]
mylist=listiterator(a)
print(next(mylist)) 
#generators return iterator object       
    
              