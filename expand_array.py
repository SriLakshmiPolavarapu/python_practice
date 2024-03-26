class Expand:
    def addEle(self, n, arr):
        new_arr = list(arr)
        
       
        
        a = 1
        while len(new_arr) > n:
            new_element = new_arr[-1] * a
            new_arr.append(new_element)
            a += 1 
        
        return new_arr

if __name__ == '__main__':
    obj = Expand()
    n = int(input("enter num")) 
    arr1 = input("enter array elements = ")
    arr1 = list(map(int, arr1.split()))
    
    res = obj.addEle(n, arr1)
    print(res)
