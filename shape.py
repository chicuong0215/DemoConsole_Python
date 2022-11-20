# init class
class Rectangle:
    def __init__(self, width, height):
        self = self
        self.name = 'Hình chữ nhật'
        self.width = width
        self.height = height

    def show_info(self):
        print(self.name)
        print('\tChiều rộng: ' + str(self.width))
        print('\tChiều dài: ' + str(self.height))
        print('\tDiện tích: ' + str(self.get_area()))
        print('\tChu vi: ' + str(self.get_circuit()))

    def get_area(self):
        return self.width * self.height

    def get_circuit(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, edge):
        super(Square, self).__init__(edge, edge)
        self.name = 'Hình vuông'


# use class
rectangle = Rectangle(3, 5)
square = Square(3)

rectangle.show_info()
square.show_info()
