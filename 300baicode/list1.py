l1 =  [[1,4,5],[1,3,4],[2,6]]
l2 =  [[1,2,3],[1,3,4],[2,6]]

l1.extend(l2)

print(l1)






# 13, sort().
# Phương thức này có tác dụng sắp xếp lại các phần tử trong list theo một thứ tự xác định.

# Cú pháp:

# python
# copy
# mylist.sort(reverse, key)
# Trong đó:

# mylist là list mà các bạn muốn sắp xếp.
# reverse là một boolean cấu hình kiểu sắp xếp. Nếu reverse = True thì list sẽ được sắp xếp từ lớn đến bé, nếu reverse = False thì list sẽ được sắp xếp theo thứ tự từ bé đến lớn. Mặc định thì reverse = False.
# key là callback def để xử lý list hoặc là một lamda function (thường được dùng để sắp xếp các list tuple hoặc dictionary).
# VD: 
list = ['A', 'C', 'B', 'E', 'D']

list.sort()
print(list)
# Kết quả: ['A', 'B', 'C', 'D', 'E']

list.sort(reverse=True)
print(list)
# Kết quả: ['E', 'D', 'C', 'B', 'A']


def custom_sort(elem):
    return elem[1]
list = [(1, 2), (5, 7), (7, 100), (4, 4)]
list.sort(key=custom_sort)
print(list)
# Kết quả: [(1, 2), (4, 4), (5, 7), (7, 100)]