class Car:
    def __init__(self,name):
        self.name=name
    
    @staticmethod
    def start():
        print("car started")
        
    def color(self,clr):
        self.clr=clr
        return self.clr
    
class Audi(Car):
    
    def type(self,typ):
        self.typ=typ
        return self.typ
    
obj=Audi()
print(obj.type("disel"))
obj.start()
print(obj.color("blie"))   
print(obj.name)      
        