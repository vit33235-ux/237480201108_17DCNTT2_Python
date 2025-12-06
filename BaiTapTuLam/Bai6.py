import math

r = float(input("Nhập bán kính hình trụ (r): "))
h = float(input("Nhập chiều cao hình trụ (h): "))

S = 2 * math.pi * r * (h + r)
V = math.pi * r**2 * h

print(f"\nDiện tích toàn phần của hình trụ: {S:.2f}")
print(f"Thể tích của hình trụ: {V:.2f}")
