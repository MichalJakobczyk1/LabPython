import math


class Shape:

    def can_exist(self):
        print("Some conditions")

    def print_figure(self):
        print("Some figure")

    def calc_perimeter(self):
        print("Some perimeter")

    def calc_area(self):
        print("Some area")


class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if not self.can_exist():
            raise ValueError("Triangle with those sides can't exist")

    def can_exist(self):
        # Sprawdź warunek nierówności trójkąta
        return 2 * self.a > self.b > 0 and self.a > 0 and self.b > 0

    def print_figure(self):
        print("This is a triangle")

    def calc_perimeter(self):
        perimeter = round(self.a + self.a + self.b, 2)

        return "Perimeter is : " + str(perimeter)

    def calc_area(self):
        # połowa obwodu
        s = (self.a + self.a + self.b)/2
        area = round((s * (s - self.a) * (s - self.a) * (s - self.b)) ** 0.5,2)

        return "Area is : " + str(area)


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if not self.can_exist():
            raise ValueError("Rectangle with those sides can't exist")

    def can_exist(self):
        # Sprawdź warunek istnienia prostokąta
        return self.a > 0 and self.b > 0

    def print_figure(self):
        print("This is a rectangle")

    def calc_perimeter(self):
        perimeter = round((self.a * 2) + (self.b * 2), 2)

        return "Perimeter is : " + str(perimeter)

    def calc_area(self):
        area = round(self.a * self.b,2)

        return "Area is : " + str(area)


class Circle(Shape):

    def __init__(self, r):
        self.r = r

        if not self.can_exist():
            raise ValueError("Circle with this radius can't exist")

    def can_exist(self):
        # Sprawdź warunek istnienia koła
        return self.r > 0

    def print_figure(self):
        print("This is a circle")

    def calc_perimeter(self):
        perimeter = round(2 * math.pi * self.r, 2)

        return "Perimeter is : " + str(perimeter)

    def calc_area(self):
        area = round(math.pi * self.r**2, 2)

        return "Area is : " + str(area)


triangle = Triangle(4,7)
triangle.print_figure()
print(triangle.calc_perimeter())
print(triangle.calc_area())

rectangle = Rectangle(3,2)
rectangle.print_figure()
print(rectangle.calc_perimeter())
print(rectangle.calc_area())

circle = Circle(3)
circle.print_figure()
print(circle.calc_perimeter())
print(circle.calc_area())

