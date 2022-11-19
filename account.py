class Account:
<<<<<<< Updated upstream
    def __init__(self,name, balance = 0):
        
        self.__account_name= name
        self.__account_balance = float(balance)
=======
#     """
#     Class that established objects for account name and account balance
#     """
    def __init__(self, name, balance = 0):
        """
        function that initialzes account name and account balance
        """
        self.__account_name= name # Establish object name
        self.__account_balance = float(balance) # Establish object value
>>>>>>> Stashed changes
    
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
 

<<<<<<< Updated upstream
def main():
    P1 = Account("John")
    print(P1.get_name())
    print(P1.get_balance())
    print(P1.deposit(100))
    print(P1.withdraw(-101))
    print(P1.get_balance())
    
if __name__ == "__main__":
    main()
=======
# def main():
#     """
#    Initial testing values that were used before test_account was created
#    """
#     P1 = Account("John",0)
#     print(P1.get_name())           #John
#     print(P1.get_balance())       # 0.0
#     print(P1.deposit(100))
#     print(P1.withdraw(90))
#     print(P1.get_balance())       #10.0
#     
# if __name__ == "__main__":
#     main()
>>>>>>> Stashed changes
