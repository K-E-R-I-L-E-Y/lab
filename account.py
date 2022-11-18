class Account:
    def __init__(self,name, balance = 0):
        
        self.__account_name= name
        self.__account_balance = float(balance)
    
    def deposit(self,amount):
        if float(amount) > 0:
            self.__account_balance =self.__account_balance + amount
            return True , self.__account_balance
        if float(amount) < 0:
            self.__account_balance = self.__account_balance
            return False

    
    def withdraw(self, amount):
        if float(amount) > self.__account_balance or float(amount) <= 0:
            self.__account_balance = self.__account_balance
            return False
        if float(amount) < self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True, self.__account_balance
    
    def get_balance (self):
        return self.__account_balance
    
    def get_name (self):
        return self.__account_name
 

def main():
    P1 = Account("John")
    print(P1.get_name())
    print(P1.get_balance())
    print(P1.deposit(100))
    print(P1.withdraw(-101))
    print(P1.get_balance())
    
if __name__ == "__main__":
    main()
