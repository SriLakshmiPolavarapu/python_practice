data=[1,2,3,[4,5],6,7]

data_op1 = [1,2]
data_op2 = [3,4]
data_op1 = data_op2
print(data_op1)
print(data_op2)


from copy import copy

data_op1 = copy(data_op2)
print(data_op1)
print(data_op2)
data_op2 = copy(data_op1)
print(data_op1)
print(data_op2)


#shallow

data1 = copy(data)

data1[2] = 12 #3 will change to 12
#data1[3] = 14 # the whole 3=> [4,5]is replaced with 14
data1[3].append(9)
print(data1)
print(data)



from copy import deepcopy

#deepcopy

user = [11,12,13,[14,15],16,17]

user1 = deepcopy(user)

user1[2] = 22
user1[3].append(19)
print(user1)
print(user)


data1 = deepcopy(data)

data1[2] = 12 #3 will change to 12
#data1[3] = 14 # the whole 3=> [4,5]is replaced with 14
data1[3].append(9)
print(data1)
print(data)

