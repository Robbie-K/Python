#Taking user input for the radius

radius = int(input("What is the radius of your circle? "))
r = radius

#import math for pi to work and creating a function to find the area and print it

import math
def area_of_circle(r):
    area = math.pi*r**2
    print("The area of the circle is: ", area)

#running the function

area_of_circle(r)

#note: I was going to use camel case but the question specifies the function name
