class Merge:
    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr
    
    def divide(self, arr1, arr2):
        arr1_a = Merge.bubble_sort(arr1)
        arr2_b = Merge.bubble_sort(arr2)
        
        combined_arr = arr1_a + arr2_b
        combine = Merge.bubble_sort(combined_arr)
        return combine 
            
                 
if __name__ == "__main__":
    obj = Merge()
    arr1 = input("enter arr1")
    arr1=list(map(int, arr1.split()))
    
    arr2 = input("enter arr2")
    arr2=list(map(int, arr2.split()))
    
    res = obj.divide(arr1, arr2)
    print(res)                   
            