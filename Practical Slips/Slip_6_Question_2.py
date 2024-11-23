# Q. 2. Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance. 

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """
        Initializes a new BankAccount object.
        """
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}.")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Amount must be positive.")

    def check_balance(self):
        """
        Prints the current balance of the account.
        """
        print(f"Current balance: ₹{self.balance}.")


# Example usage:
if __name__ == "__main__":
    # Create a BankAccount object
    account = BankAccount(
        account_number="123456789", 
        customer_name="John Doe", 
        date_of_opening="2024-11-18", 
        balance=5000
    )
    
    # Perform operations
    account.check_balance()  # Check initial balance
    account.deposit(2000)    # Deposit ₹2000
    account.withdraw(1500)   # Withdraw ₹1500
    account.withdraw(6000)   # Attempt to withdraw ₹6000 (Insufficient funds)
    account.check_balance()  # Check final balance
