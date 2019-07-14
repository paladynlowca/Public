from abc import ABC, abstractmethod
from math import sqrt, sin, cos, pi


class DescriptorReal:
    def __init__(self, name, initial_value=None):
        self.var_name = name
        self.value = initial_value
        return

    def __get__(self, obj, object_type):
        return self.value

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError('id - Incorrect data')
        self.value = value


class DescriptorColor:
    color_list = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]

    def __init__(self, name, initial_value=None):
        self.var_name = name
        self.value = initial_value
        return

    def __get__(self, obj, object_type):
        return self.value

    def __set__(self, obj, value):
        self.value = DescriptorColor.color_list[value[0]]
        print(self.value)


class DescriptorRatio:
    def __init__(self, name, initial_value=None):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, object_type):
        return self.value

    def __set__(self, obj, value):
        if 0 >= value <= 1:
            raise ValueError('id - Incorrect data')
        self.value = value


class ConvexPolygon(ABC):
    fill_color = DescriptorColor('fill_color')
    outline_color = DescriptorColor('outline_color')

    def __init__(self):
        self.attributes = {}
        return

    def check_correct(self):
        return

    @abstractmethod
    def area(self):
        return

    @abstractmethod
    def perimeter(self):
        return

    @abstractmethod
    def draw(self):
        return
    pass


# Trójkąty
class Triangle(ConvexPolygon, ABC):  # Zwykły
    pass


class EquilateralTriangle(Triangle):  # Równoboczny
    side = DescriptorReal('side')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Podstawa'}
        return

    def perimeter(self):
        return self.side * 3

    def area(self):
        return sqrt(3) / 4 * self.side ** 2

    def draw(self):
        height = sqrt(3) / 2 * self.side
        return [(self.side / 2, 0), (0, height), (self.side, height)]
    pass


class IsoscelesTriangle(EquilateralTriangle):  # Równoramienny
    side = DescriptorReal('side')
    height = DescriptorReal('height')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Podstawa', 'height': 'Wysokośc'}
        return

    def perimeter(self):
        return self.side + 2 * sqrt(self.height ** 2 + (self.side / 2) ** 2)

    def area(self):
        return self.side * self.height / 2

    def draw(self):
        return [(self.side / 2, 0), (0, self.height), (self.side, self.height)]
    pass


# Czworokąty
class ConvexQuadrilateral(ConvexPolygon, ABC):  # Zwykły
    pass


class Parallelogram(ConvexQuadrilateral):  # Równoległobok
    side_a = DescriptorReal('side_a')
    side_b = DescriptorReal('side_b')
    height = DescriptorReal('height')

    def __init__(self):
        super().__init__()
        self.attributes = {'side_a': 'Bok a', 'side_b': 'Bok b', 'height': 'Wysokośc'}
        return

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.height

    def draw(self):
        if not self.side_b == self.height:
            move = sqrt(self.side_b ** 2 - self.height ** 2)
        else:
            move = 0
        return [(move, 0), (self.side_a + move, 0), (self.side_a, self.height), (0, self.height)]

    def check_correct(self):
        if self.height > self.side_b:
            raise ValueError('id - Incorrect data')
    pass


class Kite(ConvexQuadrilateral):  # Latawiec
    diagonal_a = DescriptorReal('diagonal_a')
    diagonal_b = DescriptorReal('diagonal_b')
    ratio = DescriptorRatio('ratio')

    def __init__(self):
        super().__init__()
        self.attributes = {'diagonal_a': 'Przekątna e', 'diagonal_b': 'Przekątna f',
                           'ratio': 'Stosunek punktu\nprzecięcia'}
        return

    def perimeter(self):
        top = self.diagonal_a * self.ratio
        bottom = self.diagonal_a - top
        return 2 * (sqrt(top ** 2 + (self.diagonal_b / 2) ** 2) + sqrt(bottom ** 2 + (self.diagonal_b / 2) ** 2))

    def area(self):
        return self.diagonal_a * self.diagonal_b / 2

    def draw(self):
        top = self.diagonal_a * self.ratio
        center = self.diagonal_b / 2
        return [(center, 0), (self.diagonal_b, top), (center, self.diagonal_a), (0, top)]
    pass


class Rhombus(Parallelogram):  # Rąb
    side = DescriptorReal('side')
    height = DescriptorReal('height')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Bok', 'height': 'Wysokość'}
        return

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.height

    def draw(self):
        if not self.side == self.height:
            move = sqrt(self.side ** 2 - self.height ** 2)
        else:
            move = 0
        return [(move, 0), (self.side + move, 0), (self.side, self.height), (0, self.height)]

    def check_correct(self):
        if self.height > self.side:
            raise ValueError('id - Incorrect data')
    pass


class Square(Kite, Rhombus):  # Kwadrat
    side = DescriptorReal('side')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Bok'}
        return

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

    def draw(self):
        return [(0, 0), (self.side, 0), (self.side, self.side), (0, self.side)]

    def check_correct(self):
        return
    pass


# Reszta figur
class RegularPentagon(ConvexPolygon):
    side = DescriptorReal('side')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Bok'}
        return

    def perimeter(self):
        return self.side * 5

    def area(self):
        return sqrt(25 + 10 * sqrt(5)) / 4 * self.side ** 2

    def draw(self):
        corners = []
        r = self.side / sqrt(3 - (1 + sqrt(5)) / 2)
        for i in range(5):
            corners.append((sin(2 * pi / 5 * i) * r + r, cos(2 * pi / 5 * i) * r + r))
            pass
        return corners
    pass


class RegularHexagon(ConvexPolygon):
    side = DescriptorReal('side')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Bok'}
        return

    def perimeter(self):
        return self.side * 6

    def area(self):
        return 3 * sqrt(3) / 2 * self.side ** 2

    def draw(self):
        corners = []
        r = self.side
        move = self.side
        for i in range(6):
            corners.append((sin(2 * pi / 6 * i) * r + move, cos(2 * pi / 6 * i) * r + move))
            pass
        return corners
    pass


class RegularOctagon(ConvexPolygon):
    side = DescriptorReal('side')

    def __init__(self):
        super().__init__()
        self.attributes = {'side': 'Bok'}
        return

    def perimeter(self):
        return self.side * 8

    def area(self):
        return (1 + sqrt(2)) * 2 * self.side ** 2

    def draw(self):
        corners = []
        r = self.side * sqrt((2 + sqrt(2)) / 2)
        for i in range(8):
            corners.append((sin(2 * pi / 8 * i) * r + r, cos(2 * pi / 8 * i) * r + r))
            pass
        return corners
    pass
