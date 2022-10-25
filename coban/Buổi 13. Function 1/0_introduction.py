"""
Introduction:
=============
- Vấn đề gì khi lập trình tuần tự?
=> Tính 1 giá trị ở nhiều nơi - logic phức tạp => dẫn đến rủi ro gì, tại sao
=> làm sao hạn chế rủi ro này
+ Code dài - khó đọc, không chứa logic tường minh
- file code quá dài, lặp đi lặp lại
- gom nhóm thành 1 phần độc lập xử lý nhiệm vụ cụ thể -> cách đặt tên, cách gọi, cách tổ chư cức tường mình
+ Logic xử lý phân tán, mỗi nơi một phiên bản
- khó tìm lỗi
- không hệ thống hóa => tối ưu code không đảm bảo
"""

"""
Định nghĩa function:
- Là chương trình con, nhận nhiệm vụ cụ thể. 
- Có thể điều khiển bằng các tham số đầu vào
- Trả về kết quả cho đầu ra

func_1('a', 'b', 2)
- print()
- input()
- int(), float(), bool(), str()
- max(), min()
- enumerate(list_l)
....
=========
Khai báo function
def + tên hàm (danh sách tham số):
    ....
    thân hàm
    ...
    trả về giá trị return
    ...
-> không có return -> trả về none
-> Hàm có thể không có tham số truyền vào

-> def = define
"""

def func_name():
    print('Hello world ' * 3)

func_name()