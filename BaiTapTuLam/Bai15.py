# Đọc N từ file
with open("bieudienso.inp", "r") as f:
    N = int(f.readline().strip())

results = []

# Xét dãy liên tiếp từ độ dài 2 trở lên
for length in range(2, N+1):
    # Giả sử dãy bắt đầu từ số x, tổng S = x + (x+1) + ... + (x+length-1)
    # S = length*x + (length*(length-1))/2
    # x = (N - length*(length-1)/2) / length
    numerator = N - length * (length - 1) // 2
    if numerator <= 0:
        break
    if numerator % length == 0:
        x = numerator // length
        sequence = [str(x + i) for i in range(length)]
        results.append("+".join(sequence))

# Ghi kết quả ra file
with open("bieudienso.out", "w") as f:
    if results:
        for seq in results:
            f.write(seq + "\n")
    else:
        f.write("0\n")
