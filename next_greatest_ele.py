class Greatest:
    def nextGreatNum(self, arr):
        if len(arr) == 0:
            return -1
        for i in range(0,len(arr)):
            nxt = -1
            for j in range(i+1,len(arr)):
                if arr[i] < arr[j]:
                    nxt = arr[j]
                    break
            print(arr[i] +"---> "+nxt)        
    
if __name__ == "__main__":
    obj = Greatest()
    arr = list(map(int,input("enter array").split()))
    res = obj.nextGreatNum(arr)
    print(res)            