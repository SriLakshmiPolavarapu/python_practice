#import python1
from python1 import MyClass
class MyClass1:
    obj = MyClass()
    print(obj.global_a)
    print(obj._MyClass__private_b)
    print(obj._protected_c)
    