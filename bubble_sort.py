class Merge:
    def bubble_sort(self,arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
            return arr
    
if __name__ == "__main__":
    obj = Merge()    
    n = list(map(int, input("enter arr").split()))
    res = obj.bubble_sort(n)
    print(res)