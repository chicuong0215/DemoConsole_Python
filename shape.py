# init class
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
        for i in range(self.width):
            for j in range(self.length):
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
        if a + b > c and a + c > c and b + c > a:
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
        p = (1 / 2) * (self.a + self.b + self.c)
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


# use class
rectangle = Rectangle(3, 5)
rectangle.show_info()

square = Square(3)
square.show_info()

triangle = Triangle(3, 4, 5)
triangle.show_info()

circle = Circle(5)
circle.show_info()
