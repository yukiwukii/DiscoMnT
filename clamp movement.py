from math import *

pi = 3.14159
offsetX = 140
offsetY = 140

class Point:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def to_gcode(self):
        parts = []
        if self.x is not None:
            parts.append(f"X{self.x}")
        if self.y is not None:
            parts.append(f"Y{self.y}")
        if self.z is not None:
            parts.append(f"Z{self.z}")
        return " ".join(parts)


def convert_points_to_gcode(points):
    f = open("clamp_movement.txt", "w")
    f.write("G0 F1000 \n")

    for point in points:
        if point.x is not None:
            f.write(f"G0 X{point.x}\n")
        if point.y is not None:
            f.write(f"G0 Y{point.y}\n")
        if point.z is not None:
            f.write(f"G0 Z{point.z}\n")

    f.close()

points = []

def eject():
    points.append(Point(z=10))
    points.append(Point(z=0))
    points.append(Point(z=10))

def fill_row(reverse):
    if(reverse):
        currx = 100
        for i in range(10):
            currx -= 10
            points.append(Point(x = currx))
            eject()

    else:
        currx = 0
        for i in range(10):
            currx += 10
            points.append(Point(x = currx))
            eject()

def fill():
    reverse = False
    curry = 0
    for i in range(5):
        curry += 10
        points.append(Point(y = curry))
        fill_row(reverse)
        reverse = not reverse

fill()
convert_points_to_gcode(points)
