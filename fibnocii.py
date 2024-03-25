class fibnocii:
    def findFib(self,n):
          n = int(n)
          n1=0
          n2=1
          if n==0:
              return 0
          elif n==1:
              return n2
          else:
                for i in range(1,n):
                    sum = n1+n2
                    n1 = n2
                    n2 = sum
                return n2
        
if __name__ == '__main__':
    obj = fibnocii()
    n = input("enter num") 
    res = obj.findFib(n)
    print(res)              
            
        