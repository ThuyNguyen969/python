"""# Easy [1] Day different:
Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05"""
# 1
from datetime import datetime
def day_diff(release_date, code_complete_day):
    release_date = datetime.strptime(release_date, "%d/%m/%Y")
    code_complete_day = datetime.strptime(code_complete_day, "%Y-%d-%m")
    return (release_date - code_complete_day).days

"""# Easy [2] Alphabet and Number:
Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
Vd:
str1 = "Emma25 is Data scientist50 and AI Expert"
alpha_num(str1) == ["Emma25", "scientist50"]"""

# 2
import re
def alpha_num(sentence):
    reg = "\w+\d+"  
    regStr = re.findall(reg, sentence)
    return(regStr)
    
