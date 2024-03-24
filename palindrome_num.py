class Palindrom:
    def findPalin(self,input):
        temp = int(input)
        rev = 0
        while temp > 0:
            number = temp % 10
            rev = rev * 10 + number
            temp = temp // 10
        if input == str(rev):
            return "Yes, palindrom"
        else:
            return "Not a Palindrom"    
        
if __name__ == '__main__':
    obj = Palindrom()
    n = input("enter num") 
    res = obj.findPalin(n)
    print(res)              
            
        