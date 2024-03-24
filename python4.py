#given a list, show whether it is set or not

def is_set(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                return False
    return True

list1=[2,1,4]        
print(is_set(list1))        



# given 2 lists, show that it is not a set

def is_set1(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return False
    return True

myList1=[1,2,3,4]
myList2=[11,25,6,7]
print(is_set1(myList1,myList2))            