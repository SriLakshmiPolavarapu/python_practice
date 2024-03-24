temp = 10   # global
def func():
     temp = 20   # local
     print(temp) 
     
print(temp)   # output => 10
func()    # output => 20
print(temp)   # output => 10




temp = 10   # global
def func():
     global temp
     temp = 20   # local
     print(temp) 
     
print(temp)   # output => 10
func()    # output => 20
print(temp)   # output => 20

