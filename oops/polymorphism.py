#   method overridng
class Student:
    
    def details(self,name,age):
        self.name=name
        self.age=age
        return self.name, self.age
    
    def marks(self,english,math,science):
        self.math=math
        self.english=english
        self.science=science
        return self.math, self.english, self.science
    
    @property
    def average(self):
        self.res = ((self.math + self.science + self.english)/3)
        return self.res
        
class Teacher:
    
    def details(self,name,age):
        self.name=name
        self.age=age
        return self.name, self.age        
    
    def designation(self,text):
        self.text=text
        return self.text    

obj1 = Teacher()
print(obj1.details("Lakshmi",35))
print(obj1.designation("Senior"))

obj2 = Student()
print(obj2.details("Sri",23)) 
print(obj2.marks(100,95,98))
print(obj2.average)