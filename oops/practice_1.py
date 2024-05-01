"""
class Student:
    marks=150   #class attribute
    def __init__(self,marks):
        self.marks=marks    #object attribute
        print("added")
        
s1 = Student(100)
print(s1.marks)        
#   obj attr >>> class attr
"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("added")
        
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("Name is",self.name,"and your marks are",sum/3)
        

s1 = Student("Sri",[10,20,30])
s1.get_avg()            