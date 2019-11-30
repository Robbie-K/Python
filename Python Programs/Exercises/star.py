#Creating a star using turtle

import turtle

#Creating the screen for the turtle

graphicWindow = turtle.Screen()
graphicWindow.bgcolor("lightgreen")

#Customizing turtle

george = turtle.Turtle()
george.color("blue")
george.pensize(8)
george.hideturtle()
george.penup()
george.setposition(0,0)
george.pendown()

#Creating a for loop for the turtles movement

for i in range(5):
    george.forward(180)
    george.right(144)


graphicWindow.mainloop()
