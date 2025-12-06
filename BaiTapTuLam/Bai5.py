S = float(input("Nhập quãng đường (km): "))
v = float(input("Nhập vận tốc xe (km/h): "))

# Kiểm tra vận tốc hợp lệ
if v <= 0:
    print("Vận tốc phải lớn hơn 0!")
else:
    t = S / v
    # Đổi sang giờ và phút
    gio = int(t)
    phut = (t - gio) * 60
    print(f"\nThời gian xe đi hết quãng đường là: {t:.2f} giờ")
    print(f"Hoặc: {gio} giờ {phut:.0f} phút")
