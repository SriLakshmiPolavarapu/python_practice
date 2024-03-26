class factorial:
    def findFact(self,n):
          n = int(n)
          fact = 1
          for i in range(1,n+1):
              fact = fact * i
          return fact    
        
if __name__ == '__main__':
    obj = factorial()
    n = input("enter num") 
    res = obj.findFact(n)
    print(res)              
            
        