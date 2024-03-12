def hoan_vi(mang_gia_tri, mang_kieu_du_lieu):
     """
     Hàm hoán vị tập giá trị và kiểu dữ liệu sử dụng thuật toán đệ quy.

     Tham số:
     mang_gia_tri: Danh sách các giá trị cần hoán vị.
     mang_kieu_du_lieu: Danh sách các kiểu dữ liệu.

     Trả về:
     Danh sách các tập giá trị và kiểu dữ liệu hoán vị.
     """
     if len(mang_gia_tri) == 0:
          return [[]]
     ket_qua = []
     for i in range(len(mang_kieu_du_lieu)):
          mang_gia_tri_moi = mang_gia_tri[:]
          mang_gia_tri_moi[0] = f"{mang_gia_tri_moi[0]}-{mang_kieu_du_lieu[i]}"
          for hoan_vi_con in hoan_vi(mang_gia_tri_moi[1:], mang_kieu_du_lieu):
               ket_qua.append([mang_gia_tri_moi[0]] + hoan_vi_con)
     return ket_qua

mang_gia_tri = ["câu 1", "câu 2", "câu 3" ,"câu 4", "câu 5"]
mang_kieu_du_lieu = ["a", "b", "c", "d"]

# In số lượng hoán vị
print(len(hoan_vi(mang_gia_tri, mang_kieu_du_lieu)))

# In các hoán vị
for hoan_vi in hoan_vi(mang_gia_tri, mang_kieu_du_lieu):
     print(*hoan_vi)
