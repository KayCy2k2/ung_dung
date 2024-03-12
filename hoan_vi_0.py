def hoan_vi(chuoi):
    """
    Hàm hoán vị 1 chuỗi sử dụng thuật toán đệ quy.

    Tham số:
      chuoi: Chuỗi cần hoán vị.

    Trả về:
      Danh sách các chuỗi hoán vị.
    """
    if len(chuoi) == 0:
      return [""]
    ket_qua = []
    for i in range(len(chuoi)):
      for chuoi_moi in hoan_vi(chuoi[:i] + chuoi[i + 1:]):
        ket_qua.append(chuoi[i] + chuoi_moi)
    return ket_qua

chuoi = "abcdef"

# Tính và hiển thị số lượng hoán vị
so_luong_hoan_vi = len(hoan_vi(chuoi))
print(f"Số lượng hoán vị: {so_luong_hoan_vi}")

# In kết quả hoán vị trên 5 cột
for i in range(0, len(hoan_vi(chuoi))):
    if i % 30 == 0:
      print()
    print(f"{hoan_vi(chuoi)[i]:2}", end=" ")
