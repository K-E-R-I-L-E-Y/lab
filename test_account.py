import pytest
from account import *

class test:
    def setup_method(self):
        self.p1 = Account("Jane", 0)
        self.p2 = Account ("John", 0)
        self.p3 = Account ("Joe", 0)
        
    def teardown_method (self):
        del self.p1
        del self.p2
        
    
    def test_init(self):
        assert self.p1.get_name() == "Jane"
        assert self.p1.get_balance() == 0
        
        assert self.p2.get_name() == "John"
        assert self.p2.get_balance() == 0
        
        assert self.p3.get_name() == "Joe"
        assert self.p3.get_balance() == 0
    
    def test_deposit(self):
        assert self.p1.deposit(100) == 100
        assert self.p1.deposit(100) is True
        
        assert self.p2.deposit(-10) == 0
        assert self.p1.deposit(-10) is False
        
        assert self.p2.deposit(0) == 0
        assert self.p2.deposit(0) is False
    
    def test_withdraw(self):
        assert self.p1.withdraw(50) == 50
        assert self.p1.withdraw(50) is True
        
        assert self.p2.withdraw(-50) == 0
        assert self.p2.withdraw is False
        
        assert self.p3.withdraw(20) == 0
        assert self.p3.withdraw is False
    