# Xây dựng trang Blogs cực kỳ đơn giản

Xây dựng trang Blogs đơn giản, cho phép người dùng đăng và xem các bài post, chỉnh sửa bài post cũng như một API để tạo mẫu file .docx đơn giản
JS DOM
HTML CSS căn bản

Mô tả một số page/chức năng:

-   Trang chủ (homepage): Hiển thị tất cả các bài viết (theo thứ tự mới nhất -> cũ nhất), đồng thời có một form cho phép người dùng nhập thông tin để tạo một post mới
-   Trang cập nhật (edit): Hiển thị form kèm dữ liệu hiện tại về một bài post cụ thể, cho phép người dùng chỉnh sửa thông tin, sau đó cập nhật bài post đó
-   Trang giới thiệu (about) giới thiệu thông tin về bản thân/trang web/...
-   Trang tạo file docx (letter) hiển thị form cho phép người dùng nhập một số thông tin, tạo file .docx theo mẫu (tùy chỉnh), sau đó hiển thị link cho phép người dùng tải file về

Gợi ý các framework/library sử dụng:

-   Flask: https://flask.palletsprojects.com/en/2.0.x/
-   pymysql: https://pypi.org/project/PyMySQL/
-   python-docx: https://python-docx.readthedocs.io/en/latest/

Tham khảo ví dụ mẫu tại link sau: http://banx.pythonanywhere.com/


-----
JSDOM
Tạo 1 trang HTML với nội dung là 3 đoạn văn. Hãy viết các function có tác dụng như sau:

changeColor(): Đổi màu chữ của 3 đoạn văn theo thứ tự xanh, vàng, đỏ.
changeBgColor(color): Thay đổi màu nền của trang thành màu color.
copyContent(paragraph1, paragraph2): Thay đổi nội dung của đoạn văn paragraph1 thành giống nội dung của đoạn văn paragraph2 (tham số truyền vào là id của 2 đoạn văn hoặc thứ tự của đoạn văn).
changeFontSize(x): Thay đổi kích thước font chữ của cả 3 đoạn văn thành x pixels (x là một số nguyên).
increaseFontSize(paragraph): Tăng kích thước font chữ của đoạn văn mong muốn (tham số truyền vào là id đoạn văn hoặc thứ tự đoạn văn) lên 1 pixel so với kích thước hiện tại, kích thước tăng lên không được vượt quá 30 pixels (Sử dụng sau khi gọi hàm changeFontSize() hoặc dùng window.getComputedStyle).
decreaseFontSize(paragraph): Giảm kích thước font chữ của đoạn văn mong muốn (tham số truyền vào là id đoạn văn hoặc thứ tự đoạn văn) xuống 1 pixels so với kích thước hiện tại, kích thước giảm xuống không vượt quá 10 pixels.
Nâng cao: Tạo ra các nút ở cuối trang và gán sự kiện onclick để khi bấm nút thì gọi hàm tương ứng.

-----
HTML
Tạo 1 trang web Blog với giao diện tương tự như ảnh sau, style càng giống càng tốt.
Style đẹp, giống bản vẽ > 70%. Code HTML đúng cú pháp, đặt tên class có ý nghĩa.
Nội dung tự chuẩn bị một nội dung tử tế có ý nghĩa và không quá ngắn (ví dụ một bài báo, một mẩu chuyện, review, chia sẻ, ...).
Trong nội dung phải có ảnh minh họa, ảnh phải có thuộc tính alt và không bị méo.
Tiêu đề bài viết sử dụng thẻ h1. Nếu bài viết dài thì cần chia làm nhiều đoạn văn (dùng thẻ p) và có tiêu đề (sử dụng h2, h3, ...).
Những chỗ nào có thể bấm vào để chuyển trang thì sử dụng thẻ a, để link là # làm placeholder.