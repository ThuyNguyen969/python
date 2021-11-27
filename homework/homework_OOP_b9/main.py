"""Bổ sung thêm phương thức from_json cho class BankAccount để nạp dữ liệu từ file JSON

Đầu vào là đường dẫn file JSON (lưu ý xử lý path)
Kết quả trả về là một list accounts
Sử dụng vòng lặp, in list theo dạng bảng
Triển khai thêm phương thức magic method phù hợp để in ra với hàm print
"""
import os
import sys
import json

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
json_file = os.path.join(current_dir, "bank_accounts.json")


class BankAccount:
    minimum_balance = 50000

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
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

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

    @classmethod
    def from_json (cls1, json_file):
        accounts = []
        with open(json_file, 'r') as f:
            data = json.loads(f.read())
            
        for obj in data:
                #print(obj["account_name"])
                accounts.append(
                    cls1(obj["account_number"], obj["account_name"], int(obj["balance"])))
        return accounts

print("\nDanh sách account đọc từ file json:\n")
print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")

json_accounts = BankAccount.from_json(json_file)
for account in json_accounts:
    account.display()
