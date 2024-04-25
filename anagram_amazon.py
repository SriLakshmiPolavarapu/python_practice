class Anagram:
    def findAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return "Not anagram"
        
        list_str1={}
        list_str2={}
        
        for i in str1:
            list_str1[i] += 1
        for j in str2:
            list_str2[j] += 1
            
        if list_str1 == list_str2:
            return "Anagram"
        else:
            return "not anagram"                
        
            
    
if __name__ == "__main__":
    obj = Anagram()
    str1 = input("enter string = ")
    str2 = input("enter string = ")
    
    res = obj.findAnagram(str1, str2)
    print(res)
        
    