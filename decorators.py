from time import time
def decorator_x(func): # decorators wrap up a function and alters the behaviour of the function without altering the code
    def wrapper_func():
        print("x"*10)
        func()
        print("y"*20)
    return wrapper_func

@decorator_x
def hello():
    print("hello sally")
hello()    
#hello=decorator_func(hello)
#hello() 
def timing(func):
       def wrapper_func(*args,**kwargs):
           start=time()
           print(start)
           result=func(*args,**kwargs)
           end=time()
           print(end)
           print("time used ",end-start)

           return result
       return wrapper_func
@timing     
def myfunc(num):
    sum=0
    for i in range(num+1):
        sum+=i
    return sum 
print(myfunc(2000000))          