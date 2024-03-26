class isomorphic:
    def checkIso(self, a, b):
        if len(a) != len(b):
            return "Not Isomorphic String"
        
        for i in range(len(a)):
            for j in range(i+1, len(b)):
                if (a[i] == a[j] and b[i] != b[j]) or (a[i] != a[j] and b[i] == b[j]):
                    return "Not Isomorphic String"
        else:            
            return "Yes it is Isomorphic string"
                

if __name__ == "__main__":
    obj = isomorphic()
    a = input("Enter string 1 = ")
    b = input("Enter string 2 = ")
    
    res = obj.checkIso(a, b)
    print(res)   
                        