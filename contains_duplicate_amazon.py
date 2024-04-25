class Duplicate:
    def findDuplicate(self, arr):
        arr = list(map(int, arr.split()))
        for i in range(0, len(arr)):
            for j in range(1+i, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False                           
                
            
    
if __name__ == "__main__":
    obj = Duplicate()
    arr = input("enter array = ")
    res = obj.findDuplicate(arr)
    print(res)
        
    