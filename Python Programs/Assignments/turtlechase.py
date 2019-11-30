# Robert Karg
# Assignment 2
# 10145986

import turtle
import random
import time


# assigning keybindings
# every time any of w,a,s, or d is pressed alice moves then the boundaries are checked
# then it checks for winner, it also adds one to count in order to display the steps
def wKey():
    global count
    alex.forward(30)

    aliceMovement()
    checkBoundaries()
    checkForWinner()
    count += 1
    return

def aKey():
    global count
    alex.left(45)
    aliceMovement()
    checkBoundaries()
    checkForWinner()
    count += 1
    return

def sKey():
    global count
    alex.backward(30)
    aliceMovement()
    checkBoundaries()
    checkForWinner()
    count += 1
    return

def dKey():
    global count
    alex.right(45)
    aliceMovement()
    checkBoundaries()
    checkForWinner()
    count += 1
    return


# if alice or alex cross the boundaries it teleports them randomly inside the screen
def checkBoundaries():  #"""Smaller window maybe?"""

    if alice.xcor() > 250 or alice.xcor() <-250:
        alice.penup()
        alice.setposition(rand.randrange(-250,251),rand.randrange(-250,251))
        alice.pendown()

    elif alice.ycor() > 250 or alice.ycor() < -250:
        alice.penup()
        alice.setposition(rand.randrange(-250,251),rand.randrange(-250,251))
        alice.pendown()

    elif alex.xcor() > 250 or alex.xcor() < -250:
        alex.penup()
        alex.setposition(rand.randrange(-250,251),rand.randrange(-250,251))
        alex.pendown()

    elif alex.ycor() > 250 or alex.ycor() < -250:
        alex.penup()
        alex.setposition(rand.randrange(-250,251),rand.randrange(-250,251))
        alex.pendown()
    else:
        return


    # maximumX = 225
    # minimumX = -240
    # maximumY = 239
    # minimumY = -232
# through trial and error found max and min of the window for x and y:
# 225 is max x  239 is max y
# -240 is min x  -232 is min y

# used random to pick a number between 1 and 3 then for both 1 and 2 she moves
# forward and for 3 she switches directions randomely
def aliceMovement(): # """Does this work?"""
    move = rand.randrange(1,4)
    if move == 1 or move == 2:
        alice.forward(20)
    elif move == 3:
        direction = rand.randrange(1,3)
        if direction == 1:
            alice.left(90)
        elif direction == 2:
            alice.right(90)

# checking for the winner
def checkForWinner():
    aliceX = alice.xcor()
    aliceY = alice.ycor()
    alexX = alex.xcor()
    alexY = alex.ycor()

    global distanceBetween
    distanceBetween = ((aliceX - alexX)**2 + (aliceY - alexY)**2)**(1/2)
    if distanceBetween <= 30:
        winner()
    else:
        pen.clear()
        pen.write(("%-8s"  "%d" "%-2s" "%-34s" "%.2f" "%s" %("Step #:",count,".","Distance between Alice & Alex is:", distanceBetween,".")), font=("Arial", 12, "normal"))

def winner():
    pen.clear()
    pen.write(("%-7s"  "%d" "%-2s" "%-34s" "%.2f" %("Step #",count,":","Distance between Alice & Alex is:", distanceBetween)), font=("Arial", 12, "normal"))
    pen.penup()
    pen.setposition(0,0)
    pen.pendown()
    pen.color("green")
    pen.write("You win!!!", align = "Center", font =("Arial", 25, "normal"))
    pen.penup()
    pen.setposition(0,-20)
    pen.pendown()
    pen.write("%-12s" "%d" "%7s" %("You won in:", count, "moves!"), align = "Center", font = ("Arial", 15, "normal"))
    pen.penup()
    pen.setposition(0,-200)
    pen.pendown()
    pen.write("Game will exit in 5 seconds", align = "Center", font =("Arial", 10, "normal"))
    pen.penup()
    time.sleep(5)
    graphicWindow.bye()



def main():
    global count
    count = 1
    turtle.setup(500,500)
    global graphicWindow
    graphicWindow = turtle.Screen()
    graphicWindow.title("Chasing Alice")

    global rand
    rand = random.Random()

    # creating alice with a random postion in the window
    global alice
    alice = turtle.Turtle()
    alice.color("red")
    alice.shape("turtle")
    alice.penup()
    alice.setposition(rand.randrange(-250,251),rand.randrange(-250,251))
    alice.pendown()
    alice.speed(0)

    # creating alex at the center of the window
    global alex
    alex = turtle.Turtle()
    alex.color("blue")
    alex.shape("turtle")
    alex.speed(0)


    global pen
    pen = turtle.Turtle()
    pen.color("black")
    pen.penup()
    pen.setposition(-230,230)
    pen.pendown()
    pen.speed(0)
    pen.hideturtle()



# within meaning including 30 pixels?


# through trial and error found max and min of the window for x and y:
# 225 is max x  239 is max y
# -240 is min x  -232 is min y




    graphicWindow.listen()
    graphicWindow.onkey(wKey, "w")
    graphicWindow.onkey(aKey, "a")
    graphicWindow.onkey(sKey, "s")
    graphicWindow.onkey(dKey, "d")







    graphicWindow.mainloop()





main()
