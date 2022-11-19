import math


def run():
    print('Phương trình bậc hai có dạng: ax^2+bx+c=0')

    print('Nhập a = ')
    a = float(input())
    print('Nhập b = ')
    b = float(input())
    print('Nhập c = ')
    c = float(input())

    print('Nghiệm của phương trình:')
    delta = b * b - 4 * a * c
    if delta < 0:
        print('Phương trình vô nghiệm')
    elif delta == 0:
        print('Phương trình có nghiệm kép:')
        print('x1 = x2 = ' + str(-b / (2 * a)))
    else:
        print('Phương trình có hai nghiệm phân biệt:')
        print('x1 = ' + str((-b + math.sqrt(delta)) / (2 * a)))
        print('x2 = ' + str((-b - math.sqrt(delta)) / (2 * a)))
