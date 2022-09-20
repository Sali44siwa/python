class student:
    def __init__(self,age,name,gpa):
        self.age=age
        self.name=name
        self.gpa=gpa
        
        #enscapulation
        #private member variable cannot be accessed outside the class
class character:
    def __init__(self,weight,height):
        self.__weight=weight #private variables
        self.__height=height
    def public_method(self):
        self.__weight
        print("private variables can be called only inside the class")
        self.__private_method()
    def set_weight(self,value):
        self.__weight=value
    def get_weight(self):
        return self.__weight
    def set_height(self,value):
        self.__height=value
    def get_height(self):
        return self.__height 
    def __private_method(self): #private method and can not be used outside the class
        print("private method only used within the class")
              
hello=character(45,30)
hello.set_weight(34)

print(hello.get_height())

print(hello.get_weight())
hello.public_method()      
     