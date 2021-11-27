"""Khai báo class SavingAccount kế thừa từ BankAccount, bổ sung:
monthly_interest_rate: Lãi suất hàng tháng = 0.005
calculate_interest(): tính tiền lãi hàng tháng, công thức balance * monthly_interest_rate
Tạo class Customer bao gồm một số thông tin:
name, date_of_birth, email, phone
get_info() hiển thị thông tin Customer
Thay đổi class BankAccount:
_account_name thành _owner là một Customer
display() hiển thị thông tin số tài khoản, thông tin khách hàng và số dư"""

class BankAccount:
    def __init__(self, account_number, owner , balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number    

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"\n| Số tài khoản {self.account_number} | Thông tin KH: {self._owner.get_info()} | Số dư: {self.balance} |\n")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")  


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005
    def calculate_interest(self):
        return self.monthly_interest_rate*self.balance

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"{self.name}, {self.date_of_birth}, {self.email}, {self.phone}"    

cus = Customer("ocnho","02/12/1988","thuynt26@onemount.com","0123456789")
bank_account = SavingAccount("88888888", cus, 10000000) 
bank_account.display() 
print(f"\tLãi: {bank_account.calculate_interest()}")