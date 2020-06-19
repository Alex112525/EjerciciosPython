class Figure:
    _base = 0
    _height = 0
    _num_sides = 0
    _area = 0
    _perimeter = 0

    def __init__(self, num_sides):
        self._num_sides = num_sides

class Rectangle(Figure):

    def __init__(self, base=1, height=1):
        self._num_sides = 4
        self._base = base
        self._height = height

    def calc_area(self):
        return self._base * self._height

    def calc_perimeter(self):
        return (self._base * 2) + (self._height * 2)

class Triengle(Figure):

    def __init__(self, base=1, height=1):
        self._num_sides = 3
        self._base = base
        self._height = height

    def calc_area(self):
        return (self._base * self._height) / 2

    def calc_perimeter_eq(self):
        return self._base * 3

    def calc_perimeter(self, side1=1, side2=1, side3=1):
        return side1 + side2 + side3
