class Parenthesis:
    def valid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False 
                val = stack.pop()  
                if val == '(' and i != ')':
                    return False  
                elif val == '[' and i != ']':
                    return False  
                elif val == '{' and i != '}':
                    return False  
        return len(stack) == 0  

if __name__ == "__main__":
    obj = Parenthesis()
    s = input("Enter parentheses = ")
    res = obj.valid(s)
    if res:
        print("Valid")
    else:
        print("Not Valid")
