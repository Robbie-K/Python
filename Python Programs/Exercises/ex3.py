#function for clockwise compass
#creating using elif and returning the clockwise values to end the function

def turn_clockwise(x):
    if x == "N":
        return('E')
    elif x == "E":
        return('S')
    elif x == "S":
        return('W')
    elif x == "W":
        return('N')
    else:
        return('None')


#grade function
#created using elif and returning each mark and grade for the specified increments

def grade(x):
    x = float(x)
    if x >= 75:
        return(x,"First")
    elif 70 <= x < 75:
        return(x,"Upper Second")
    elif 60 <= x < 70:
        return(x,"Second")
    elif 50 <= x < 60:
        return(x,"Third")
    elif 45 <= x < 50:
        return(x,"F1 Supp")
    elif 40 <= x < 45:
        return(x,"F2")
    elif 0 <= x < 40:
        return(x,"F3")
    else:
        return("Error, please use a valid mark!")

grade(75)
grade(60)
