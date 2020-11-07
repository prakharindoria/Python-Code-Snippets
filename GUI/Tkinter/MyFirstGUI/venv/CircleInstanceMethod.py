import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):

        self.area = 3.14 * self.radius * self.radius
        print("Area is ", self.area)

    def cal_circum(self):
        self.circum = 3.14 * self.radius * 2
        print("Area is ", self.circum)


r = int(input("Enter Radius:"))
cobj = Circle(r)
cobj.cal_area()
cobj.cal_circum()

