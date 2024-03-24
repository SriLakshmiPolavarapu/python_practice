# map

numbers = [11, 2, 3, 14, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))


def function(a):
    return a+2
result = map(function, numbers)
print(list(result))



#sorted

print(sorted(numbers))
print(sorted(numbers, reverse=True))


words=('one','three','four','sevens')

word='srilu'
print(sorted(word))

list1=[{'id':1,'name':'sri'}, {'id':2,'name':'lakshmi'},{'id':3,'name':'srilu'}]
print(sorted(list1, key=lambda x: x['id'], reverse=True))

data=(1,2,3)
print(sorted(data, key=lambda y:y, reverse=True))

data1=[(1,'one'),(2,'two')]
print(sorted(data1, key=lambda y:(y[1],y[-1]), reverse=True))



#filter

data2=[1,2,3,'none',4,5]
print(list(filter(lambda x:x == 'none', data2)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))