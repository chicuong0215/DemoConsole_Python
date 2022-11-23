while True:
    print('Phương trình bậc nhất có dạng: ax+b=0')

    print('Nhập a = ', end='')
    a = float(input())
    print('Nhập b = ', end='')
    b = float(input())

    print(str(a) + 'x' + (' + ' if b > 0 else ' - ') + str(abs(b)) + ' = 0')
    print('Nghiệm của phương trình:')
    if a != 0:
        if b == 0: print('x = 0')
        if b != 0: print('x = ' + str(-b / a))
    if a == 0:
        if b == 0: print('Vô số nghiệm!')
        if b != 0: print('Vô nghiệm!')

    print('Bạn có muốn tiếp tục? (y/n): ')
    if str.lower(input()) == 'n': break
