class NonRepeating:
    def checkChar(self, str):
        
        empty = {}
        if len(str) == 0:
            return "False"
        
        for char in str:
            if char in empty:
                empty[char] += 1
            else:
                empty[char] = 1
                
                
        for char in str:
            if empty[char]== 1:
                return char
            
        return None
    
if __name__ == "__main__":
    obj = NonRepeating()
    s = input("Enter string = ")
    res = obj.checkChar(s)
    if res:
        print(res)
    else:
        print("False")       
            