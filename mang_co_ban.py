# Cách 1: Sử dụng danh sách Python

# Tạo mảng 1 chiều với các số nguyên
mang_so_nguyen = [1, 2, 3, 4, 5]

# Tạo mảng 1 chiều với các chuỗi
mang_chuoi = ["a", "b", "c", "d", "e"]

# Tạo mảng 1 chiều với các kiểu dữ liệu khác nhau
mang_hop = [1, "a", 3.14, True, None]

----------------------------------------------------------
# Cách 2: Sử dụng thư viện NumPy

import numpy as np

# Tạo mảng 1 chiều từ danh sách
mang_np = np.array([1, 2, 3, 4, 5])

# Tạo mảng 1 chiều với các giá trị đều bằng 1
mang_np_1 = np.ones(5)

# Tạo mảng 1 chiều với các giá trị cách đều nhau
mang_np_2 = np.arange(1, 10, 2)
