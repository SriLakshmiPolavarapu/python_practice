class reverse1:
    #method-1
    def rev1(self, str):
        rev_word = ' '.join(reversed(str.split()))
        return rev_word
    
    #method-1
    def rev2(self, str):
        str = str.split()
        rev_word = ""
        for i in range(len(str)-1, -1, -1):
            rev_word = rev_word + str[i] + " "
        return rev_word
    
    #method-2
    def rev3(self, str):
        str = str.split()
        rev_word = ""
        new_rev_word=""
        for i in range(len(str)-1, -1, -1):
            rev_word = rev_word + str[i] + " "
            # world hello
            for j in range(len(str[i])-1, -1, -1):
                new_rev_word = new_rev_word + str[i][j]
            new_rev_word = new_rev_word + " "
        return new_rev_word.strip()    
    
    #method-3
    def rev4(self, str):
        str = str.split()
        rev_word = ""
        for i in range(len(str)):
            for j in range(len(str[i])-1, -1, -1):
                rev_word = rev_word + str[i][j]
            rev_word += " "
        return rev_word        
            


if __name__ == "__main__":
    obj = reverse1()
    a = input("Enter string = ")
    res = obj.rev1(a)
    res1 = obj.rev2(a)
    res2 = obj.rev3(a)
    res3 = obj.rev4(a)
    
    
    print(res)   
    print(res1)
    print(res2)
    print(res3)
                        