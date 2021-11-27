'''Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, và triển khai thêm các phương thức:
get_account_number()
get_account_name()
get_balance()
set_balance() - balance phải lớn hơn hoặc bằng 0
Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.

Chú ý:
Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
Với deposit(), amount phải lớn hơn 0
Nếu giá trị không phù hợp thì thông báo ra console'''

class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance                

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(self.account_number, self.account_name, self.balance, "₫")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


my_account = BankAccount(9999999, "ocnho", 100000)
my_account.deposit(200000)
my_account.display()

my_account.withdraw(50000)  
my_account.display()
