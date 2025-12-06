a,b,c=eval(input('Nhập vào 3 số cách nhau bởi dấu phẩy: '))
if(a+b>c)and(b+c>a)and(c+a>b):
    if a*a*b==c*c or a*a*c==b*b or c*c+b*b==a*a:
        print('Đây là tam gic vuông')
    elif a==b==c:
        print('Đây là tam giác đều')
    elif a==b or a==c or c==b:
        print('Đây là tam là giác cân')
    else:
        print('Đây là tam giác thường')
else:
    print('Đây không phải 3 canh của tam giác')