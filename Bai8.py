a, b, c = eval(input('Nhap vao 3 so cach nhau boi dau phay: '))
if (a + b > c) and (b + c > a) and (c + a > b):
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print('Đây la tam giác vuông')
    elif a == b == c:
        print('Đây là tam giác đèu')
    elif b == c or b == a or a == c:
        print('Đây la tam giac can')
    else:
        print('Day là tam giac thường')
else:
    print('Day khong phai la ba canh cua tam giac')