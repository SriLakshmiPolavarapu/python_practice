class Account:
    __password = "abc123"   #private attribute
    
    def details(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        return self.acc_number, self.name
    
    def __location(self,loc):   #private method
        self.__loc = loc
        return self.__loc
        
    def result(self):
        print(self.details("Sri", "12345"))
        print(self.__password)
        print(self.__location("hyd"))
        
    @staticmethod    
    def message():
        print("hey")
        
a = Account()
a.message()
a.result()           