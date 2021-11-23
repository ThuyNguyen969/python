# Bài 5: Print Star
# Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:
# Bài 5 - Hình 1:
print("Bài 5 - Hình 1: chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng")
n = int(input("Nhập số dòng: "))
i = 1
j = n-1
sao = '*'
space = ' '
for i in range(1,n+1):
    print(space*j, sao*i)
    i += 1
    j -= 1

# Bài 5 - Hình 2:
print("Bài 5 - Hình 2: chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng")
n = int(input("Nhập số dòng - khi in sẽ đảo ngược: "))
i = 1
j = n-1
sao = '*'
space = ' '
for i in range(1,n+1):
  if(i==n):
    print(space*j,sao*n*2)      
  else:
    print(space*j,sao*i) 
  i+=1
  j-=1
for j in range(1,n+1):
  i-=1
  if(i!=n):
    print(space*n,sao*i) 

# Bài 4: Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
#my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
#Trả ra {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}
print("Bài 4: Đếm số")
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2,
           2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
print("\tList cần đếm số: ",my_list)
arr = {}
for i in range(len(my_list)):
    key = my_list[i]
    if(key not in arr):
        arr[key] = 1
    else:
        arr[key] = arr[key] + 1
print("\tKết quả: ",arr)


# Bài 3: Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
"""vd in ra sau mỗi 5s:
Countdown to Xmas 2021: 112 days, 11:47:01.339588
Countdown to Xmas 2021: 112 days, 11:46:56.324008
Countdown to Xmas 2021: 112 days, 11:46:51.310473"""
###Tổ trưởng/ Giáo viên nếu chạy cả file thì bỏ comment phần số lần cần hiển thị n, i để dừng sớm như mog muốn nhé

print("Bài 3: Đếm ngược đến XMas 2021")
import time
import datetime
sleep = int(input("\tNhập thời gian cần đợi (s): "));
#n = int(input("\tSố lần cần hiển thị: "));
#i = 1;
now = datetime.datetime.now()
xmas = datetime.datetime(2021, 12, 25, 0, 0, 0)
t = xmas - now;
#while (t and i <= n):
while t:
    now = datetime.datetime.now()
    #i+=1;
    print('\tCountdown to Xmas 2021: ' +str(xmas - now));
    time.sleep(sleep)


# bài 2: Unique value Dictionary:
"""Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
#[VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất."""
print("Bài 2: Unique value Dictionary")
def unique_value_dict(mydict):
    list=[]
    set1=set()
    for i in mydict:
        value = i.values()
        for j in value:
            list.append(j)
    set1=set(list)
    print("\tGiá trị duy nhất của value",set1)

list_1= [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
list_2=[dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]

unique_value_dict(list_1)
unique_value_dict(list_2)

# Bài 1: Find Pair
# cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
# Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
# vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []
print("Bài 1: Find Pair")
A = [3, 6, 7, 9, 11, 12]
length = len(A)
sum = int(input("\tNhập tổng cần so sánh: "))
output = []
for i in range(0, length-1):
    for j in range(i+1, length):
        if(A[i] + A[j] == sum):
            output.append('(' + str(A[i]) + ',' + str(A[j])+')')
            break
else:
    print("\tCác cặp số cần tìm: ",output)
