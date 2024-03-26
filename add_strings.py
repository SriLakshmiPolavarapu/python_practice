
class Add:
    def addStr(self, a, b):
       
       a = int(a)
       b = int(b)
       sum = a + b
       return str(sum)
       
if __name__ == "__main__":
    obj = Add()
    a = input("Enter string 1 = ")
    b = input("Enter string 2 = ")
    
    res = obj.addStr(a, b)
    print(type(res))   
                        