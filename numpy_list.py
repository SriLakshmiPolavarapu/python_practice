import numpy as np
import time

# using list
my_list = [1,2,3]

start_time = time.time()
#result1 = map(lambda x:x*2, my_list)
result1=[x*2 for x in my_list]
end_time = time.time()

print(list(result1))
print(end_time-start_time)


# using numpy
my_list = [1,2,3]
my_numpy = np.array(my_list)
start_time = time.time()
#result2 = map(lambda x:x*2, my_numpy)
result2 = my_numpy*2
end_time = time.time()

print(list(result2))
print(end_time-start_time)

numpy1 = np.array([1,2,3], ndmin = 4)
print(numpy1)

# delete
numpy2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
add_new = np.array([[10,11,12]])

res = np.delete(numpy2, 1, axis=0)
print(res)

#sort
numpy2 = np.array([[11,2,13],[4,15,6],[27,8,19]])

res1 = np.sort(numpy2.view('i8,i8,i8'),
               order = ['f2'],
               axis=0).view(np.int64)
print(res1)
