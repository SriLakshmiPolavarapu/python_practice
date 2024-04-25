def check_dup(arr):
    duplicates_list = set()
    for i  in range(len(arr)):
        if arr[i] in duplicates_list:
            return False
        else:
            duplicates_list.add(arr[i])
    return True


def check_dup_hash(arr1):
    duplicates_hash = {}
    for i in range(len(arr1)):
        if arr[i] in duplicates_hash:
            duplicates_hash[arr[i]] +=1
        else:
            duplicates_hash[arr[i]] = 1
    for c in duplicates_hash.values():        
        if c > 1:
            return True
    return False            


arr = [2,2,3,1]
#print(check_dup(arr))  

arr1=[2,3,1,7]
#print(check_dup_hash(arr1)) 
        
        
def check_dup_sort(arr):
    arr.sort()
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
            
    return False

arr = [9, 2, 3, 1]
#print(check_dup_sort(arr))  # Output should be False
        

def check_dup_sort1(arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
               return True
            
    return False

arr = [9, 2, 3, 1]
#print(check_dup_sort1(arr))  # Output should be False
        
        
def remove_dup(arr):
    dup1={}
    dup2={}
    for i in range(len(arr)):
        if arr[i] in dup1:
            dup2[arr[i]] =1
        else:
            dup1[arr[i]]=1
            
    return dup1

arr=[1,2,3,3,4,4,5]
res = remove_dup(arr)
#print(res)
#print(len(res))          


def remove_dup(arr):
    dup1=set()
    dup2=set()
    for i in range(len(arr)):
        if arr[i] in dup1:
            dup2.add(arr[i])
        else:
            dup1.add(arr[i])
            
    return dup1

arr=[1,2,3,3,4,4,4,4,4,5]
res = remove_dup(arr)



def duplicate1(nums, k):
    hash = {}
    for index, ele in enumerate(nums):
        if ele in hash:
            if index - hash[ele] <= k:
                return True
            
            hash[ele] = index
    return False

nums = [1,2,3,2]
k = 2
#print(duplicate1(nums,k))        



def dup_zero(arr):
    i=0
    while i < len(arr)-1:
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i+=2
        else:
            i+=1
    return arr            
            
arr=[1,0,2,0,4,5]
print(dup_zero(arr))                     
        