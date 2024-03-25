class Prime:
    def checkPrime(self,n):
        if n==0 or n==1:
            return "not prime"
        elif n > 1:
            for i in range(2,n-1):
                if n%i==0:
                    return "Not prime"
            else:
                return "it is prime"
            

if __name__ == "__main__":
    obj = Prime()
    n = int(input("enter number"))
    res = obj.checkPrime(n) 
    print(res)          