class Person:
    
    def eyes(self,color):
        self.color=color
        return self.color
    
    def nose(self,shape):
        self.shape=shape
        return self.shape
    
class Features(Person):
    def __init__(self):
        pass
    
    def details(self,name):
        self.name=name
        return self.name
        
obj = Features()  
print(obj.details("Sri"))
print(obj.eyes("blue")) 
  
        