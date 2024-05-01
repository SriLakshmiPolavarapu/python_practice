class Person:
    
    @staticmethod
    def msg():
        print("start coding")
        
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

class Characteristics(Features):
    def attitute(self,txt):
        self.txt = txt
        return self.txt
        
obj = Characteristics()  

obj.msg() 
print(obj.details("Sri"))
print(obj.eyes("blue")) 
print(obj.nose("sharp"))
  
        