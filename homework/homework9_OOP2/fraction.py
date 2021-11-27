"""Tạo class Fraction (phân số)
Hàm khởi tạo nhận 2 giá trị nr (tử số) và dr (mẫu số)
Nếu dr âm, chuyển dấu cho nr (VD: 1/-2 => -1/2)
Triển khai phương thức phù hợp để in ra phân số (VD: print(fr) => -1/2)
Viết hàm hcf tìm ước chung lớn nhất của nr và dr
Thêm phương thức reduce rút gọn phân số (gọi trong __init__)
Nếu nr == 0, chỉ in ra 0
Nếu dr == 0, raise ZeroDevisonError
Nếu dr == 1, chỉ in ra nr
Triển khai các phương thức phù hợp cho phép +-*/ với 2 Fraction hoặc 1 Fraction với 1 số (int hoặc float), kết quả trả về 1 Fraction mới"""

import os
import sys
import json

class Fraction:
    minimum_balance = 50000

    def __init__(self, nr, dr):
        self.nr = nr
        self.dr = dr
        
    @property
    def nr(self):
        return self._nr

    @property
    def dr(self):
        return self._dr

    @nr.setter
    def nr(self, nr):
        self._nr = nr
        
    @dr.setter
    def dr(self, dr):
        if dr == 0:
            raise ValueError("ZeroDevisonError, phải khác 0")
        elif dr < 0:
            dr = abs(dr)
            self.nr = (self.nr)*-1
        self._dr = dr

    def display(self):
        if self.nr == 0: 
            print(0)
        elif self.dr == 1:
            print(self.nr)
        else:
            print(f"{self.nr}/{self.dr}")

    def hcf(self):
        x, y = abs(self.nr), abs(self.dr)
        hcf = x if x < y else y

        while hcf > 0:
            if x % hcf == 0 and y % hcf == 0:
                break
            hcf -= 1
        return hcf if hcf > 0 else None

    def reduce(self):
        n = self.hcf()
        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)

fr = Fraction(126, 150)
print("Phân số: ", )
fr.display()

print('\nUCLN là: ',fr.hcf())

print("\nGiá trị sau khi reduce: ")
fr.reduce()
fr.display()
