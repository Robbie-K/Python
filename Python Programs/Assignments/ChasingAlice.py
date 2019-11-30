# Robert Karg
# Assignment 2
# 10145986

import turtle
import random
import time


# used to check if alice or alex cross the screen boarders and if they have
# it resets them in a random location
def checkBoundaries(alice, alex, constHalfWindow):
    rand = random.Random()  # the random object for using random numbers
    # .xcor finds the x coordinate of the turtle and .ycor finds the
    #  y coordinate of the turtle
    if alice.xcor() > constHalfWindow or alice.xcor() < (-1 * constHalfWindow):
        alice.penup()
        alice.setposition(rand.randrange(-1 * constHalfWindow, constHalfWindow + 1),
                          rand.randrange(-1 * constHalfWindow, constHalfWindow + 1))
        alice.pendown()

    elif alice.ycor() > constHalfWindow or alice.ycor() < (-1 * constHalfWindow):
        alice.penup()
        alice.setposition(rand.randrange(-1 * constHalfWindow, constHalfWindow + 1),
                          rand.randrange(-1 * constHalfWindow, constHalfWindow + 1))
        alice.pendown()

    elif alex.xcor() > constHalfWindow or alex.xcor() < (-1 * constHalfWindow):
        alex.penup()
        alex.setposition(rand.randrange(-1 * constHalfWindow, constHalfWindow + 1),
                         rand.randrange(-1 * constHalfWindow, constHalfWindow + 1))
        alex.pendown()

    elif alex.ycor() > constHalfWindow or alex.ycor() < (-1 * constHalfWindow):
        alex.penup()
        alex.setposition(rand.randrange(-1 * constHalfWindow, constHalfWindow + 1),
                         rand.randrange(-1 * constHalfWindow, constHalfWindow + 1))
        alex.pendown()


# used random to pick a number between 1 and 3 then for both 1 and 2 she moves
# forward and for 3 she switches directions randomely
def aliceMovement(alice):
    rand = random.Random()
    move = rand.randrange(1, 4)  # random number from 1 to 3

    if move == 1 or move == 2:  # forward 2/3 moves
        alice.forward(20)
    elif move == 3:  # randomely changes direction either left or right
        direction = rand.randrange(1, 3)
        if direction == 1:
            alice.left(90)
        elif direction == 2:
            alice.right(90)


# all the movements corresponding to the specified keys
def alexMovement(alex, key):
    if key == "w":
        alex.forward(30)
    elif key == "a":
        alex.left(45)
    elif key == "s":
        alex.backward(30)
    elif key == "d":
        alex.right(45)


# finding the distance between alice and alex
def findDistanceBetween(alice, alex):
    aliceX = alice.xcor()
    aliceY = alice.ycor()
    alexX = alex.xcor()
    alexY = alex.ycor()
    # using pytha
    distanceBetween = ((aliceX - alexX)**2 + (aliceY - alexY)**2)**(1 / 2)
    return distanceBetween  # passing distanceBetween along


# checking to see if alice and alex come within 30 pixels of eachother
# if they do it runs the winner function
def checkForWinner(alice, alex, pen, count):
    distanceBetween = findDistanceBetween(alice, alex)

    if distanceBetween <= 30:
        winner(alice, alex, pen, count)

    else:
        pen.clear()
        # writes the steps as they occur (using placeholders)
        pen.write(("%-8s"  "%d" "%-2s" "%-34s" "%.2f" "%s" % ("Step #:", count, ".",
                                                              "Distance between Alice & Alex is:", distanceBetween, ".")), font=("Arial", 12, "normal"))
        return False  # in order to use the while loop


# function that runs once distanceBetween is less than or equal to 30 pixels
def winner(alice, alex, pen, count):
    center = 0  # constsnt for the middle of the screen (will always be 0)
    distanceBetween = findDistanceBetween(alice, alex)
    pen.clear()  # clears everytime to make sure the step and distanceBetween numbers dont overlap
    pen.write(("%-8s"  "%d" "%-2s" "%-34s" "%.2f" "%s" % ("Step #:", count, ".",
                                                          "Distance between Alice & Alex is:", distanceBetween, ".")), font=("Arial", 12, "normal"))
    # the above line writes the last step as normal

    pen.penup()
    pen.setposition(center, center)  # puts pen in the center of the screen
    pen.pendown()

    # writes a "victory statement"
    pen.color("green")
    pen.write("You win!!!", align="Center", font=("Arial", 25, "normal"))
    pen.penup()
    pen.setposition(center, center - 20)
    pen.pendown()
    pen.write("%-12s" "%d" "%7s" % ("You won in:", count, "moves!"),
              align="Center", font=("Arial", 15, "normal"))
    pen.penup()
    pen.setposition(center, center - 200)
    pen.pendown()
    pen.write("Game will exit in 5 seconds", align="Center", font=("Arial", 10, "normal"))
    pen.penup()
    time.sleep(5)  # i use a timer to end the game subtly
    exit()  # i opted to exit the screen instead of ending the while loop because it is less abrupt


# setups the screen for the turtles, includes a title and then returns the screen name
def creatingTurtleWindow(constWindow):
    turtle.setup(constWindow, constWindow)
    graphicWindow = turtle.Screen()
    graphicWindow.title("Chasing Alice")
    return graphicWindow


# used to create each turtle then returns the turtle
def creatingTurtle(turtleName, graphicWindow, constWindow, color):
    graphicWindow = turtle.Screen()
    turtle.setup(constWindow, constWindow)
    turtleName = turtle.Turtle()
    turtleName.shape("turtle")
    turtleName.color(color)
    return turtleName


# initial setup of alice, spawns her at a random location in the canvas
def aliceSetup(alice, constHalfWindow):
    rand = random.Random()
    alice.penup()
    alice.setposition(rand.randrange(-1 * constHalfWindow, constHalfWindow + 1),
                      rand.randrange(-1 * constHalfWindow, constHalfWindow + 1))
    alice.pendown()


# sets up the turtle i am using as a pen, thus the name
def penSetup(pen, constHalfWindow):
    speed = 0  # constant for the speed of the pen turtle, 0 disables animation so the turtle moves relatively instantly
    pen.penup()
    pen.hideturtle()
    pen.setposition(-1 * constHalfWindow + 20, constHalfWindow - 20)
    pen.pendown()
    pen.speed(speed)


# the main function which uses all the other functions in one way or another
def main():
    constWindow = 500  # constant for the size of screen (x and y)
    constHalfWindow = constWindow / 2  # constant for the max/min of the window
    count = 0  # used later for counting steps and displaying them
    # using functions to create and setup the turtles and the window
    graphicWindow = creatingTurtleWindow(constWindow)
    alice = turtle
    alex = turtle
    pen = turtle
    alice = creatingTurtle(alice, graphicWindow, constWindow, "red")
    alex = creatingTurtle(alex, graphicWindow, constWindow, "blue")
    pen = creatingTurtle(pen, graphicWindow, constWindow, "black")
    aliceSetup(alice, constHalfWindow)
    penSetup(pen, constHalfWindow)
    # note alex doesn't need seting up since he starts at 0,0

    # while loop that takes keys from the user in command line as long as
    # checkForWinner is False
    while checkForWinner(alice, alex, pen, count) == False:
        key = str(input("Please use w,a,s, or d keys to control Alex (blue): "))

        if key == "w" or key == "a" or key == "s" or key == "d":
            count += 1  # increaseing count for each key
            # these functions move alex based on the key entered, then moves alice randomely
            # then checks boundaries of the turtles and then checks if the user has won
            alexMovement(alex, key)
            aliceMovement(alice)
            checkBoundaries(alice, alex, constHalfWindow)
            checkForWinner(alice, alex, pen, count)
        # in case the user enters more than one key or any other key than w,a,s,d
        else:
            print("Please enter the correct keys(One letter at a time).")


main()
