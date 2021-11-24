"""# Medium [1] Anagram Number:
Viết hàm anagram_number() có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
vd: anagram_number(121121) == True
    anagram_number(1254) == False"""
def anagram_number(number):
    number1 = list(str(number))
    number2 = list(reversed(number1))
    if str(number2)==str(number1):
        return True
    else:
        return False

"""
# Medium [2] Roman to Integer
Các chữ số La Mã được thể hiện bằng bảy biểu tượng khác nhau: I, V, X, L, C, D và M với
I=1; V=5; X=10; L=50; C=100; D=500; M=1000

Ví dụ: số 2 được viết là II bằng số La Mã, chỉ là hai chữ I được thêm vào với nhau. 12 được viết là XII, đơn giản là X + II. Con số 27 được viết là XXVII, là XX + V + II.

Chữ số La mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, số 4 không viết là IIII mà được viết là IV. Bởi vì I đứng trước V, chúng ta lấy 5 - 1 = 4. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:

I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
X có thể được đặt trước L (50) và C (100) để tạo ra 40 và 90.
C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
Cho một chữ số la mã dạng string, hãy viết hàm roman_to_int() chuyển nó thành một số nguyên.
"""
 
def roman_to_int(roman):
    lama = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = roman.upper()
    number = 0
    while roman:
        if len(roman) == 1:
            number += lama[roman[0]]
            roman = roman[1:]
        elif lama[roman[0]] >= lama[roman[1]]:
            number += lama[roman[0]]
            roman = roman[1:]
        else:
            number += lama[roman[1]] - lama[roman[0]]
            roman = roman[2:]
    return number
