from math import *

import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

pi = 3.14159
offsetX = 140
offsetY = 155

def circle(step, radius):
    point = []
    for i in range(int(step) + 1):
        stepInRadian = 2 * pi / step * i
        pointX = radius * cos(stepInRadian)
        pointY = radius * sin(stepInRadian)
        point.append([round((pointX + offsetX), 4), round((pointY + offsetY), 4)])
    return point

def spiral(step):
    point = []
    for i in range(int(step) + 1):
        stepInRadian = 8 * pi / step * i
        pointX = stepInRadian * cos(stepInRadian)
        pointY = stepInRadian * sin(stepInRadian)
        point.append([round((pointX + offsetX), 4), round((pointY + offsetY), 4)])
    return point

def spirograph(step, a, b):
    point = []
    for i in range(int(step) + 1):
        stepInRadian = 50 * pi / step * i
        pointX = ((a-b) * cos(stepInRadian) + b * cos(stepInRadian * (a/b) -1)) * 2
        pointY = ((a-b) * sin(stepInRadian) + b * sin(stepInRadian * (a/b) -1)) * 2
        point.append([round((pointX + offsetX), 4), round((pointY + offsetY), 4)])
    return point


def convertToGcode(points):
    f = open("spiral.txt", "w")
    f.write("G0 F1000 \n")
    for i in points:
        f.write("G0" + " X" + str(i[0]) + " Y" + str(i[1]) + "\n")
    f.close()

# points = circle(100, 50) # A circle with 5cm radius
# points = spiral (100)
points = spirograph(1000, 87, 19) # can play with the values of a and b to get different structures
convertToGcode(points)
xPoint = []
yPoint = []
for j in points:
    xPoint.append(j[0])
    yPoint.append(j[1])
print(xPoint)
plt.plot(xPoint, yPoint, 'r*')
plt.axis([0, 240, 0, 300])
plt.show()
