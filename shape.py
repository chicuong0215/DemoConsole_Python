import math


class Rectangle:
    def __init__(self, width, length):
        self = self
        self.name = 'Hình chữ nhật'
        self.width = width
        self.length = length

    def show_info(self):
        print(self.name)
        print('\tChiều rộng: ' + str(self.width))
        print('\tChiều dài: ' + str(self.length))
        print('\tDiện tích: ' + str(self.get_area()))
        print('\tChu vi: ' + str(self.get_circuit()))

        self.draw()

    def draw(self):
        for i in range(int(self.width)):
            for j in range(int(self.length)):
                print('*', end=" ")
            print()

    def get_area(self):
        return self.width * self.length

    def get_circuit(self):
        return 2 * (self.width + self.length)


class Square(Rectangle):
    def __init__(self, edge):
        super(Square, self).__init__(edge, edge)
        self.name = 'Hình vuông'


class Triangle:
    def __init__(self, a, b, c):
        self.is_triangle = False
        if a + b > c and a + c > b and b + c > a:
            self.is_triangle = True
            self.a = a
            self.b = b
            self.c = c

    def show_info(self):
        if self.is_triangle:
            print('Hình tam giác')
            print('\tDộ dài cạnh a: ' + str(self.a))
            print('\tDộ dài cạnh b: ' + str(self.b))
            print('\tDộ dài cạnh c: ' + str(self.c))
            print('\tDiện tích: ' + str(self.get_area()))
            print('\tChu vi: ' + str(self.get_circuit()))
        else:
            print('Không phải hình tam giác!')

    def get_area(self):
        p = (1 / 2) * self.get_circuit()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_circuit(self):
        return self.a + self.b + self.c


class Circle:
    def __init__(self, r):
        self = self
        self.name = 'Hình tròn'
        self.r = r

    def show_info(self):
        print(self.name)
        print('\tBán kính: ' + str(self.r))
        print('\tDiện tích: ' + str(self.get_area()))
        print('\tChu vi: ' + str(self.get_circuit()))

    def get_area(self):
        return math.pi * self.r * self.r

    def get_circuit(self):
        return 2 * math.pi * self.r


def run():
    while True:
        print("Chức năng")
        print("\t1. Hình chữ nhật")
        print("\t2. Hình vuông")
        print("\t3. Hình tam giác")
        print("\t4. Hình tròn")
        print("Lựa chọn: ", end='')
        selection = int(input())
        if selection == 1:
            print("Hình chữ nhật")
            print("Nhập chiều dài và chiều rộng hình chữ nhật")
            print("Chiều dài: ", end='')
            length = float(input())
            print("Chiều rộng: ", end='')
            width = float(input())
            Rectangle(width, length).show_info()
        if selection == 2:
            print("Hình vuông")
            print("Nhập độ dài cạnh hình vuông: ", end='')
            a = float(input())
            Square(a).show_info()
        if selection == 3:
            print("Hình tam giác")
            print("Nhập độ dài 3 cạnh của tam giác")
            print("a = ", end='')
            a = float(input())
            print("b = ", end='')
            b = float(input())
            print("c = ", end='')
            c = float(input())
            Triangle(a, b, c).show_info()
        if selection == 4:
            print("Hình tròn")
            print("Nhập bán kính hình tròn: ", end='')
            r = float(input())
            Circle(r).show_info()

        print('\nBạn có muốn tiếp tục? (y/n): ')
        if str.lower(input()) == 'n': break


# test
run()
