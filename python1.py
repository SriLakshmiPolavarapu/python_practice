
#with class
class MyClass:
    #global
    global_a=10
    #private
    __private_b=20
    #protected
    _protected_c=30

    def func(self):
        print(self.global_a)
        print(self.__private_b)
        print(self._protected_c)
        
    def only_for_private(self):
        return self.__private_b  
    
    def globalMethod(self):
        print("public method")
        return self.global_a
        
    def _protectedMethod(self):
        print("protected method")
        return self._protected_c
        
    def __privateMethod(self):
        print("private method")  
        return self.__private_b
                  
    
obj=MyClass()
print(obj.global_a)    
#print(obj.__private_b) #error
print(obj._MyClass__private_b)
print(obj.only_for_private())
print(obj._protected_c)

print(obj.globalMethod())
print(obj._protectedMethod())
print(obj._MyClass__privateMethod())