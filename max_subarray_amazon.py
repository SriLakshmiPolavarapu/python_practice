class MaxSum:
    def findSubarray(self, arr):
        arr = list(map(int, arr.split()))
        sum = 0
        max_sum = float('-inf')

        for i in range(0,len(arr)):
            sum += arr[i]
            if sum < 0:
                sum = 0
            max_sum = max(sum, max_sum)
        return max_sum                    
                
            
    
if __name__ == "__main__":
    obj = MaxSum()
    arr = input("enter array = ")
    res = obj.findSubarray(arr)
    print(res)
        
    
    
    # kandane algo