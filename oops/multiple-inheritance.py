class Car:
    def color(self,clr):
        self.clr=clr
        return self.clr
    
class Bus:
    def size(self,sz):
        self.sz=sz
        return self.sz
    
class Vehicle(Car, Bus):
    @staticmethod
    def results():
        print("car and bus")      
        
obj = Vehicle()
print(obj.color("blue"))
print(obj.size("100cm"))        