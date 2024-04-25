class TwoSum:
    def findPos(self, arr, target):
        arr = list(map(int, arr.split()))
        target = int(target)
        for i in range(0,len(arr)):
            for j in range(i+1, len(arr)):
                add = arr[i] + arr[j]
                if add == target:
                    return [i, j]
        return "not found"
    
if __name__ == "__main__":
    obj = TwoSum()
    arr = input("enter array = ")
    target = input("enter target = ")
    res = obj.findPos(arr, target)
    print(res)
        
    