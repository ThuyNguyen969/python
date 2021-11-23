'''### Bài 1: Function - Đếm loại ký tự ### 
Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:
s = "Hello World! 123"
Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
a) Viết hàm trên dùng bất kỳ hàm built in nào của python
b) Viết hàm chỉ dùng 1 hàm built in duy nhất.
Gợi ý: Bộ ký tự đơn giản in ra màn hình được còn được gọi là bộ mã ASCII (đọc là 'As key') nguyên gốc gồm 128 ký tự. Bạn có thể in ra thử với câu lệnh sau.
ASCII = "".join(chr(x) for x in range(33, 128))
print(ASCII)
'''
'a. Viết hàm trên dùng bất kỳ hàm built in nào của python'

s = input("Bài 1 - Nhập chuỗi cần đếm: ")
def count_char_type(s):
    dict = {"LETTERS": 0, "CASE": {"UPPER CASE": 0, "LOWER CASE": 0}, "DIGITS": 0}
    for i in s:
        if i.isalpha():
            dict["LETTERS"] += 1
            if i.isupper():
                dict["CASE"]["UPPER CASE"] += 1
            elif i.islower():
                dict["CASE"]["LOWER CASE"] += 1
        elif i.isdigit():
            dict["DIGITS"] += 1
    return dict

print("\t KQ dùng nhiều hàm built in: ", count_char_type(s))

'b. Viết hàm chỉ dùng 1 hàm built in duy nhất'
"""
ASCII = "".join(chr(x) for x in range(48, 57))
print(ASCII)

ASCII = "".join(chr(x) for x in range(65, 90))
print(ASCII)

ASCII = "".join(chr(x) for x in range(97, 122))
print(ASCII)
"""

def count_char_type(s):
    dict = {"LETTERS": 0, "CASE": {"UPPER CASE":0, "LOWER CASE":0}, "DIGITS":0}
    for i in s:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            dict["LETTERS"] +=1
            if 65 <= ord(i) <= 90:  
                dict["CASE"]["UPPER CASE"] += 1                   
            elif 97 <= ord(i) <= 122:
                dict["CASE"]["LOWER CASE"] += 1
        elif 48 <= ord(i) <= 57: 
            dict["DIGITS"] += 1      
    return dict

print("\t KQ dùng 1 hàm built in: ", count_char_type(s))
print("\n ######")

'''### Bài 2: Function - Chỉ số thống kê mô tả ### 
Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:
giá trị trung bình (mean) của dãy.
trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.

Vd:
A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] ==> (mean(A), median(A), mode(A)) == (6.55, 7.0, [9])
B=[4,4,5,4,5,5] thì (mean(B), median(B), mode(B)) == (4.5, 4.5, [4,5])
'''

def mean(mylist):
    mylistsx = sorted(mylist)
    print('Bài 2: Điểm học sinh sau khi sắp xếp lại: ', mylistsx)
    mean = round(sum(mylistsx)/len(mylistsx), 2)
    return mean

def median(mylist):
    mylistsx = sorted(mylist)
    i = len(mylistsx)
    j =  i // 2
    if (i % 2 == 1):
        return mylistsx[j]
    else:
        median1 = j
        median2 = j - 1
        return round((mylistsx[median1] + mylistsx[median2])/2,2)

from statistics import mode
from statistics import multimode
def mode(mylist):
    return(multimode(mylist))

diem = [7, 8, 9, 2, 10, 8, 9, 9, 9, 4, 5, 8, 1, 5, 7, 7, 8, 7, 1, 10]

print("\t Điểm trung bình là: ", mean(diem))
print("\t Điểm trung vị là: ", median(diem))
print("\t Mode là: ", mode(diem))
