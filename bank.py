class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = 0.0
    
    def deposite(self, amount: float) -> None:
        """Deposite the money into bank
        
        :param amount: Money that you will be deposite into bank.
        :return: Does not return anything.
        """
        self.balance += amount

    
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the bank account.

        :param amount: Amount that you want to withdraw from bank account.
        :return None: Does not return anython from here.
        """
        
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
    def show_balance(self) -> float:
        """
        Show the balance.

        :return current balance: Available balance returns.
        """
        return self.balance


my_book = Bank(name='Ravi')
print("Name:", my_book.name)
print("Balance:", my_book.balance)

my_book.deposite(500)

print("Name:", my_book.name)
print("Balance:", my_book.balance)    

my_book.withdraw(200)

print("Name:", my_book.name)
print("Balance:", my_book.balance)

print("Balance:", my_book.show_balance())