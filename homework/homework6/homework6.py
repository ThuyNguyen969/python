"""Logfile của webserver apache gồm nhiều dòng với mỗi dòng có định dạng như sau

10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET xxxxxx HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"

Trong đó xxxxxx có thể là đường dẫn đến một thư mục hoặc file bất kỳ của server.
Dùng regex để lọc lấy ra tất cả các đường dẫn đến file .jpg trong các file log đầu vào dưới đây.
Loại bỏ các đường dẫn trùng nhau và trả ra danh sách các đường dẫn.
Định dạng của mỗi đường dẫn trả ra trong list nên là:
"http://host/path" với

host là phần cuối của tên logfile
path là phần xxxxxx được trích xuất phía trên
Input Logfiles"""

import sys
import re

def readfile_regex_image(filename):
    f =  open(filename, encoding='utf-8-sig')
    content = f.read()
    data_find = re.findall("GET (.*\.jpg)", content, re.MULTILINE)
    if(data_find):
        domain = get_domain(filename)
        #loại bỏ image trùng
        data = set(data_find) 
        inc = 1;
        print ("Danh sách ảnh trong file: ")
        for path in data:
            print(f"{inc}. {domain}{path}")
            inc += 1
    else:
        print ("Không có link ảnh trong file")        

    
def get_domain(filename):
    #regex như này thì đuôi file là google.com.vn vẫn hiểu được
    re_host = re.search("[\.](\w*(\.[a-z]{2,6}){1,2})$", filename) 
    if re_host: domain = "http://"+re_host.groups()[0]
    else: domain = ""
    return domain

###
def main():
    if len(sys.argv) != 2:
        print('usage: ./homework6.py file')
        sys.exit(1)

    filename = sys.argv[1]
    readfile_regex_image(filename)
    sys.exit(1)

if __name__ == '__main__':
  main()
