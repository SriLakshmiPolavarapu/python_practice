from typing import List

class Letters:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return "False"
        
        container = {"2": "abc", 
                 "3": "def", 
                 "4": "ghi", 
                 "5": "jkl", 
                 "6": "mno", 
                 "7": "pqrs", 
                 "8": "tuv", 
                 "9": "wxyz"}
        empty = []
        
        def backtrack(combination, nxt):
            if not nxt:
                empty.append(combination)
                return
            
            for i in container[nxt[0]]:
                backtrack(combination + i, nxt[1:])
        
        backtrack("", digits)
        return empty 
    
    
if __name__ == "__main__":
    obj = Letters()
    print(obj.letterCombinations("23"))
    print(obj.letterCombinations("34"))
    print(obj.letterCombinations(""))
    
    
    
        