class Student:
    
    def average(self,math,science):
        self.math=math
        self.science=science
        return self.math, self.science
    
    def average(self,math,science,english):
        self.math=math
        self.science=science
        self.english=english
        return self.math, self.science, self.english
    

obj1 = Student()
obj1.average(98,95)
obj1.average(89,92,94)    
        