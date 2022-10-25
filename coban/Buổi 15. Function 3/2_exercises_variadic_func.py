"""
Viết hàm chấp nhận số lượng bất kỳ đối số, có thể là các đối số thường hoặc đối số có tên (named argument, ví dụ a=10, b=15 trong lời gọi hàm func(a=10, b=15)

Tính min, max các args là số và tích của value các kwargs là số

kwargs = keyword arguments
""" 

def my_fun(*args, **kwargs):
    for idx, item in enumerate(args):
        if not (type(item) in (int, float)):
            continue

        if idx == 0: # số đầu tiên gán luôn cho giá trị lớn nhất, nhỏ nhất
            min_val, max_val = item, item
        # từ số thứ 2, so sánh và gán lại
        else:
            if min_val > item:
                min_val = item
            
            if max_val < item:
                max_val = item

    result_product = 1
    for k, v in kwargs.items(): # kwargs là dictionary
        if type(v) in (int, float):
            result_product *= v

    return min_val, max_val, result_product


print(my_fun(1, 2, -1, 'a', True, False, 1, 2, 10, 60, a=10, b=20, c='a'))