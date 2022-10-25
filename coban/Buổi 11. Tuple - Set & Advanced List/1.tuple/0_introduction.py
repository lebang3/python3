"""
Tuple là dạng bộ giá trị
- Bộ 3 số (1, 2, 3)
- Bộ hỗn hợp (1, 'a', [1, 2])
"""

t1 = (1, 2, 3)
print(t1, type(t1))

t2 = ('a',)
print(t2, type(t2))

fake_one_element_tuple = ('a' + 'b') * 3
print(fake_one_element_tuple, type(fake_one_element_tuple))

one_element_tuple = ('a' + 'b',) * 3
print(one_element_tuple, type(one_element_tuple))

"""
Để khai báo tuple 1 phần tử (element,)
-> do nếu k có , -> hiểu thành 1 giá trị nằm trong ngoặc
"""

"""
Tuple không support gán -> nó là "hằng số" -> immutable data type
t1[1] = 3
print(t1, type(t1))
"""