class BankAccount():
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def __repr__(self):
        '''unambiguous representation of the object'''
        return self.__class__.__name__ + '(' + repr(self.name) + ', ' + repr(self.balance) + ')'

    def __str__(self):
        '''string representation of object, for humans
        __repr__ is used if __str__ does not exist'''
        return self.name + ' has ₹' + str(self.balance) + ' in the bank'
   
    def __add__(self, other):
        return self.__class__(self.name + ' + ' + other.name, 
                           self.balance + other.balance - 5.95)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")