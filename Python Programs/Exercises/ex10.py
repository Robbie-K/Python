""" Robert Karg
Exercise 10 """

# both default classes from the textbook

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    # perimeter method: returns the perimeter of the rectangle
    def perimeter(self):
        return 2 * self.width + 2 *  self.height

    # flip method: switches the height and witdh values
    def flip(self):
        temp = [self.height, self.width]
        self.height = temp[1]
        self.width = temp[0]

# default class from the textbook
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x, y):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

# test function from the text
import sys
def test(did_pass):
    """  Print the result of a test.  """
    lineNum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        message = "Test at line {0} passed".format(lineNum)
    else:
        message = ("Test at line {0} FAILED.".format(lineNum))
    print(message)

# test suite with suggested cases from the textbook
def test_suite():
    test(r.perimeter() == 30)
    test(b.width == 10 and b.height == 5)
    b.flip()
    test(b.width == 5 and b.height == 10)

# creating the rectangles
r = Rectangle(Point(0, 0), 10, 5)
b = Rectangle(Point(100, 50), 10, 5)


test_suite()
