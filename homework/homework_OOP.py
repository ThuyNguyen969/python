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
        self._balance = balance

    def display(self):
        print(self._account_number, self._account_name, self._balance, "₫")

    def withdraw(self, amount):
        self._balance -= amount

    def deposite(self, amount):
        self._balance += amount


my_account = BankAccount(1, "Ba", 0)