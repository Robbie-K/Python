#Importing turtle, creating the graphic window, and creating the turtle

import turtle
graphicWindow = turtle.Screen()
graphicWindow.bgcolor("lightblue")
graphicWindow.title("Squares")
lisa = turtle.Turtle()
lisa.color("darkorange")

size = 20

#Creating a function to draw a square

def draw_Square(t , size):
    for i in range(4):
        t.forward(size)
        t.left(90)

#creating a function to recenter the turtle for draw_Square to work properly

def recenter(t):
    for i in range(1):
        lisa.penup()
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        lisa.pendown()

#creating a function that uses both to draw squares with 20 size difference
numSquares = int(input("How many squares would you like? "))
def draw_Squares(lisa,size):
    for i in range(numSquares):
        lisa.hideturtle()
        draw_Square(lisa,size)
        recenter(lisa)
        size = size + 20



#finally drawing the squares

draw_Squares(lisa,size)

#making sure the window doesn't automatically close when the function finishes running

graphicWindow.mainloop()
