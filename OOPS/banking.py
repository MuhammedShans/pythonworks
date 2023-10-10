from abc import ABC,abstractmethod

class Banking_app(ABC):

    @abstractmethod
    def fundtransfer(self):
        pass

    @abstractmethod
    def Balanceenquiry(self):
        pass

    @abstractmethod
    def Transactionhistory(self):
        pass

class Googlepay(Banking_app):

    def fundtransfer(self):
        print("Transfering fund....")

    def Balanceenquiry(self):
        print("Your Curent  balance is....")    

    def Transactionhistory(self):
        print("Your transaction history....")     

obj=Googlepay()    
obj.fundtransfer()
obj.Balanceenquiry()
obj.Transactionhistory()       