# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """
    bal = 0;
    fee = 0;
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.bal = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.bal += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        if (self.bal - amount) < 0:
            self.bal -= 5;
            self.bal -= amount;
            self.fee += 5;
        else:
            self.bal -= amount;
        
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.bal
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee

my_account = BankAccount(10)

my_account.withdraw(15)

my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()        