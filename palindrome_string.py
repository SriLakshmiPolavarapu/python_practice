class Palindrom:
    def findPalinStr(self,str):
        print(type(str))
        
        for i in range(0, int(len(str)/2)):
            if str[i] != str[len(str)-i-1]:
                return "Not a palindrom"
            else:
                return "A Palindrom"    
        
if __name__ == '__main__':
    obj = Palindrom()
    str = input("enter string = ") 
    res = obj.findPalinStr(str)
    print(res)              
            
        