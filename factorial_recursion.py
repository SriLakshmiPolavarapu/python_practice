class fibnocii:
    def findRecursiveFib(n):
          if n < 1:
              return n
          return fibnocii.findRecursiveFib(n-1) + fibnocii.findRecursiveFib(n-2)
        
if __name__ == '__main__':
    obj = fibnocii()
    n = input("enter num") 
    res = obj.findRecursiveFib(n)
    print(res)              
            
        