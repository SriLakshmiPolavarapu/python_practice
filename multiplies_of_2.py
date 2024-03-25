class Solution:
    def mult(self, arr):
        arr=[int(x) for x in arr.split()]
        for i in range(0,len(arr)):
            if arr[i] <= 100:
                    arr[i] *= 2
        return arr                    

if __name__ == "__main__":
    obj = Solution()
    arr = input("enter arr")      
    res=obj.mult(arr)
    print(res)  