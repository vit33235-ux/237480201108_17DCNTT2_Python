n = int(input("Nhập số nguyên dương n: "))
Even = 0
Odd = 0
Tam = n

while Tam > 0:
    ChuSo = Tam % 10
    if ChuSo % 2 == 0:
        Even += 1
    else:
        Odd += 1
    Tam //= 10

print(f"Số {n} có {Even} chữ số chẵn và {Odd} chữ số lẻ.")
