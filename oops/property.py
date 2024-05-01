'''
class Student:
    def __init__(self,math,english):
        self.math=math
        self.english=english
        self.percent = str((self.english + self.math)/2) + "%"
        
obj = Student(85,95)
print(obj.percent) 

# tecahers changes the marks       

obj.english = 90
obj.math = 95
print(obj.percent)  #it will still prints old percentage

'''

class Student:
    def __init__(self,math,english):
        self.math=math
        self.english=english
        
    @property
    def calResult(self):
        self.percent = str((self.english + self.math)/2) + "%"
        return self.percent

obj = Student(85,95)
print(obj.calResult)

obj.math = 98
obj.english = 89
print(obj.calResult)
        
            


