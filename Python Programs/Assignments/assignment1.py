#Assignment 1
#Robert Karg
#10145986

# taking input from sample.dat using stdin

xCenter,yCenter = eval(input())
radiusOfCirc = eval(input())
xOne,yOne = eval(input())
xTwo,yTwo = eval(input())

# equations to find values for a,b and c based on all of the inputed values

a = (xTwo - xOne)**2 + (yTwo - yOne)**2
b = 2 * ((xOne - xCenter) * (xTwo - xOne) + (yOne - yCenter) * (yTwo - yOne))
c = (xOne - xCenter)**2 + (yOne - yCenter)**2 - radiusOfCirc**2


alphaOne = (-b + (b**2 - 4*(a)*(c))**(.5))/(2*a) # -b + ... alpha value
alphaTwo = (-b - (b**2 - 4*(a)*(c))**(.5))/(2*a) # -b - ... alpha value


quadRoot = (b**2 - (4*a*c))  #just so there is no need to retype this several times

intSwap = 0 # incase the intercept values need to be switched
numIntercepts = 0 # for the findNumIntercepts() function

 # finds the number of intercepts

def findNumIntercepts():
    global numIntercepts
    if (quadRoot < 0):                  # the three basic cases
        numIntercepts = 0
    elif (quadRoot == 0):
        numIntercepts = 1
    elif (quadRoot > 0):
        numIntercepts = 2
        # the rest are cases where the line is within the circle and there are no intercepts
        # or some cases not seen in the samples that i wanted to make sure worked properly
        # ex: if the line intercepts very close to the bottom of the circle, etc.
        if ((xCenter + radiusOfCirc > xTwo) and (xCenter - radiusOfCirc < xOne)):
            numIntercepts = 0
        elif ((xOne < xCenter - radiusOfCirc) and (xTwo == xCenter + radiusOfCirc)):
            numIntercepts = 2
        elif ((yTwo == yCenter) or (yOne == yCenter)):
            numIntercepts = 1
            if ((xTwo > xCenter + radiusOfCirc) and (xOne < xCenter - radiusOfCirc)):
                numIntercepts = 2
        elif (xOne == xCenter):
            numIntercepts = 1
        elif ((yOne < yCenter - radiusOfCirc) and (yTwo > yCenter - radiusOfCirc)):
            numIntercepts = 1
            global intSwap  # i noticed in this case the values for intercept
                            # one and 2 needed to be switched so i added an intercept
                            # swaping piece
            intSwap = 1
        elif ((yCenter + yOne <= yCenter + radiusOfCirc) or (yCenter - yOne >= yCenter - radiusOfCirc)) \
        and ((yCenter + yTwo <= yCenter + radiusOfCirc) or (yCenter - yTwo >= yCenter - radiusOfCirc)):
            if ((yOne == yTwo) and ((xTwo > xCenter +radiusOfCirc) and ( xOne < xCenter - radiusOfCirc))):
                return()
            numIntercepts = 0

    else:
        numIntercepts = 2
        return()
    return()

# the intercept values found using alpha and xOne, xTwo and, yOne, yTwo

xIntOne = ((1 - alphaOne)* xOne) + (alphaOne * xTwo)
yIntOne = ((1 - alphaOne)* yOne) + (alphaOne * yTwo)

xIntTwo = ((1 - alphaTwo)* xOne) + (alphaTwo * xTwo)
yIntTwo = ((1 - alphaTwo)* yOne) + (alphaTwo * yTwo)

# importing and creating a graphicWindow, jim the turtle, etc.

import turtle
graphicWindow = turtle.Screen()
graphicWindow.setworldcoordinates(0,0,800,600)

jim = turtle.Turtle()

# function for drawing the main circle

def drawBigCircle():
    jim.penup()
    jim.setposition(xCenter, yCenter - radiusOfCirc)
    jim.pendown()
    jim.circle(radiusOfCirc)           # drawing the circle
    return()

# function for drawing the line between (xOne,yOne) and (xTwo,yTwo)

def drawAlphaLineSegment():
    jim.penup()
    jim.setposition(xOne, yOne)
    jim.pendown()
    jim.setposition(xTwo, yTwo)
    return()

# drawing both circles for the start and end of the line

smallCircRadius = 6      # to be used for the radius of circles at intercepts and
                         # at the beginning and end of the line

def drawStartEndCircles():
    jim.penup()
    jim.setposition(xOne, yOne - smallCircRadius)
    jim.pendown()
    jim. circle(smallCircRadius)
    jim.penup()
    jim.setposition(xTwo, yTwo - smallCircRadius)
    jim.pendown()
    jim.circle(smallCircRadius)
    return()


 # function for drawing the intercept circles

def drawCircleIntercepts():
    global numIntercepts  # so this function can use these variables
    global xIntOne
    global xIntTwo
    global yIntTwo
    global yIntOne
    if (numIntercepts > 0):
        global intSwap
        if (intSwap == 1):      # in case the intercept values need to be switched
            xIntOne = xIntTwo
            yIntOne = yIntTwo

        jim.penup()
        jim.setposition(xIntOne, yIntOne - smallCircRadius)  # intercept 1
        jim.pendown()
        jim.circle(smallCircRadius)


    if (numIntercepts > 1): # intercept 2
        jim.penup()
        jim.setposition(xIntTwo, yIntTwo - smallCircRadius)
        jim.pendown()
        jim.circle(smallCircRadius)
    else:
        return()
    return()


# running all functions to display the circle, line, and all intercepts

findNumIntercepts()
drawBigCircle()
drawAlphaLineSegment()
drawStartEndCircles()
drawCircleIntercepts()


graphicWindow.mainloop()  # so the graphicWindow does not close automatically
