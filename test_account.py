# from pytest import *
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')
        
    def teardown_method(self):
        del self.a1
        
    def test_init(self):
        assert self.a1.get_name() == 'John'
        pass
    
    def test_deposit(self):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) is False
        assert self.a1.get_balance() == 1.5
    
    def test_withdraw(self):
        assert self.a1.withdraw(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(50) is True
        assert self.a1.withdraw(-100) is False
        assert self.a1.get_balance() == 50

        assert self.a1.deposit(50) is True
        assert self.a1.withdraw(50) is True
        assert self.a1.get_balance() == 0
