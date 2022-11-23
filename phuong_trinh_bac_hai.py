import math

while True:
    print('Phương trình bậc hai có dạng: ax^2+bx+c=0')

    print('Nhập a = ', end='')
    a = float(input())
    print('Nhập b = ', end='')
    b = float(input())
    print('Nhập c = ', end='')
    c = float(input())

    print(str(a) + 'x^2' + (' + ' if b > 0 else ' - ') + str(abs(b)) + 'x' + (' + ' if c > 0 else ' - ') + str(
        abs(c)) + ' = 0')
    print('Nghiệm của phương trình:')
    delta = b * b - 4 * a * c
    if delta < 0:
        print('Phương trình vô nghiệm!')
    elif delta == 0:
        print('Phương trình có nghiệm kép:')
        print('x1 = x2 = ' + str(-b / (2 * a)))
    else:
        print('Phương trình có hai nghiệm phân biệt:')
        print('x1 = ' + str((-b + math.sqrt(delta)) / (2 * a)))
        print('x2 = ' + str((-b - math.sqrt(delta)) / (2 * a)))

    print('Bạn có muốn tiếp tục? (y/n): ')
    if str.lower(input()) == 'n': break
