from datetime import datetime

class bank:

    bank_name:str
    acno:int
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):

        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} rs available balance is {self.balance}")    

    def withdrawal(self,amount):
        if amount>self.balance:
            print("Transaction failed insufficient balance")
        else:    
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} rs available balance is {self.balance}")    

    def get_balance(self):
        print(f"your {self.bank_name} A/c {self.acno} available balance on {datetime.today()} is {self.balance}")        


obj1=bank()
obj1.create("sbi",123456,"shan","savings",50000)  
# obj1.deposit(20000)   .
#obj1.withdrawal(1000)
obj1.get_balance()

obj2=bank()
obj2.create("sbi",321457,"kishor","savings",5000)
# obj2.deposit(1000)
# obj2.withdrawal(10000)
obj2.get_balance()