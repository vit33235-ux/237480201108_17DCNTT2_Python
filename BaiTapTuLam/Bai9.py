tien = int(input("Nhập số tiền (VNĐ): "))
To_Menh_Gia = [50000, 20000, 10000, 5000, 2000, 1000]
print("\nSố tờ tiền tương ứng:")
for MenhGia in To_Menh_Gia:
    SoTo = tien // MenhGia
    tien %= MenhGia
    if SoTo > 0:
        print(f"{MenhGia:>6,} VNĐ : {SoTo} tờ")
