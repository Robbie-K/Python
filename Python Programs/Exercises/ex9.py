# Robert Karg - Exercise 9

# part one: editing the distance function to take in two Points
# calculating distance between the two specified Points
def distance(point1, point2):
    distance = ((point2.x - point1.x)**2 + (point2.y - point1.y)**2)**(1/2)
    return distance

class Point:
    """ Create a new point on the xy- plane"""

    # constructor: just gives the object the x and y values given
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # part two: reflecting a point over the x-axis
    # I simply nultiply the y-value of the point by -1 to accomplish this
    def reflect_x(self):
        self.y = self.y * -1
        return (self.x, self.y)

# creating the points:
pt1 = Point(1, 2)
pt2 = Point(4, 6)
pt3 = Point(3, 5).reflect_x()  # this is a new reflected point, (3, -5)

# printing the results:
# print(distance(pt1, pt2))
# print(pt3)
