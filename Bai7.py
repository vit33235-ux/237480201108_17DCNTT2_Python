a = int(input('Nhap vao so nguyen duong a= '))
b = int(input('Nhap vao so nguyen duong b= '))
c = int(input('Nhap vao so nguyen duong c = '))
if (a + b > c) and (b + c > a) and (c + a > b):
    print("Ba so vua nhap cau thanh 1 tam giac")
else:
    print("Ba so vua nhap khong cau thanh 1 tam giac")