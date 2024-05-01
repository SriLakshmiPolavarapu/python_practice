#   create account class with two attributes - balnace and account number
#   create methods for debit, credit and printing the balance


class Account:
    
    def __init__(self,balance,acc_num):
        self.balance=balance
        self.acc_num=acc_num
        print("coding start")
        
    def get_credit(self,credit_amt):
        self.balance += credit_amt
        print("credited ",credit_amt)  
            
        
    def get_debit(self,debit_amt):
        self.balance -= debit_amt
        print("debited ",debit_amt) 
        
    def get_balance(self):
        print("total balance is",self.balance)
                
        
obj = Account(1000,1234)
obj.get_credit(500)
obj.get_debit(100)
obj.get_balance()           