print("=== XÉT ĐẬU CHUYÊN ===")

# Nhập điểm từng môn
Toan = float(input("Nhập điểm Toán: "))
Van = float(input("Nhập điểm Văn: "))
Anh = float(input("Nhập điểm Tiếng Anh: "))

# Tính điểm trung bình
dtb = (Toan + Van + Anh) / 3
print(f"Điểm trung bình: {dtb:.2f}")

# Xét điều kiện
if dtb >= 8.5 and Toan >= 9 and Toan > Van and Toan > Anh:
    print("→ Đậu chuyên Toán.")
elif dtb >= 8.5 and Van >= 9 and Van >= Anh:
    print("→ Đậu chuyên Văn.")
elif dtb >= 8.5 and Anh >= 8.0:
    print("→ Đậu chuyên Tiếng Anh.")
elif dtb >= 8.5:
    print("→ Đậu chuyên Tin học.")
else:
    print("→ Không đậu chuyên.")
