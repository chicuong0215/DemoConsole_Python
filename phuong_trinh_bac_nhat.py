def run():
    print('Phương trình bậc nhất có dạng: ax+b=0')

    print('Nhập a = ')
    a = float(input())
    print('Nhập b = ')
    b = float(input())

    print('Nghiệm của phương trình:')
    if a != 0:
        if b == 0: print('x = 0')
        if b != 0: print('x = ' + str(-b / a))
    if a == 0:
        if b == 0: print('Vô số nghiệm!')
        if b != 0: print('Vô nghiệm!')
