# Parent Class: Bank
class Bank:
    bank_name = "HDFC"
    Ifsc = "HDFC000578"
    branch = "HBR LAYOUT"

    def __init__(self, Customer_name, accno, location, pin, balance, phone, email=None):
        self.Customer_name = Customer_name
        self.accno = accno
        self.location = location
        self._pin = pin
        self._balance = balance
        self.phone = phone
        self.email = email

    # Abstraction: Hides internal data with clean interface
    def Customer_Details(self):
        print("Customer Details")
        print(f'Name: {self.Customer_name}\nAcc No: {self.accno}\nLocation: {self.location}\nPhone: {self.phone}\nEmail: {self.email}')

    # Encapsulation: Using protected variables and method access
    def check_balance(self):
        userpin = int(input("Enter the PIN: "))
        if self._pin == userpin:
            print(f'Account balance: ₹{self._balance}')
        else:
            print("Wrong PIN")

    def deposit(self):
        userpin = int(input("Enter the PIN: "))
        if self._pin == userpin:
            amount = int(input("Enter the deposit amount: "))
            self._balance += amount
            print(f'New balance after deposit: ₹{self._balance}')
        else:
            print("Wrong PIN")

    def withdraw(self):
        userpin = int(input("Enter the PIN: "))
        if self._pin == userpin:
            amount = int(input("Enter the withdrawal amount: "))
            if amount <= self._balance:
                self._balance -= amount
                print("Transaction successful")
                print(f'Remaining balance: ₹{self._balance}')
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")


# Inheritance: Subclass from Bank
class LoanAccount(Bank):

    def __init__(self, Customer_name, accno, location, pin, balance, phone, loan_amount, email=None):
        super().__init__(Customer_name, accno, location, pin, balance, phone, email)
        self.loan_amount = loan_amount

    # Polymorphism: Overriding Customer_Details
    def Customer_Details(self):
        super().Customer_Details()
        print(f'Loan Amount Approved: ₹{self.loan_amount}')


# Object Creation
Customer1 = LoanAccount("Madhusai", "45677891", "MITS", 1234, 3000, 9347241524, 50000)

# Menu UI
def options():
    while True:
        choice = int(input(
            "\nChoose an option:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Customer Details\n0. Exit\nEnter: "))
        match choice:
            case 1:
                Customer1.deposit()
            case 2:
                Customer1.withdraw()
            case 3:
                Customer1.check_balance()
            case 4:
                Customer1.Customer_Details()
            case 0:
                print("Exited.")
                break
            case _:
                print("Invalid choice.")

options()
