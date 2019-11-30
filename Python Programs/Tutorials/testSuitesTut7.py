import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def day_name(d):
    if (d == 0):
        return("Sunday")
    elif (d == 1):
        return("Monday")
    elif (d == 2):
        return("Tuesday")
    elif (d == 3):
        return("Wednesday")
    elif (d == 4):
        return("Thursday")
    elif (d == 5):
        return("Friday")
    elif (d == 6):
        return("Saturday")
    else:
        return(None)

test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)

def day_num(n):
    if (n == "Sunday"):
        return(0)
    elif (n == "Monday"):
        return(1)
    elif (n == "Tuesday"):
        return(2)
    elif (n == "Wednesday"):
        return(3)
    elif (n == "Thursday"):
        return(4)
    elif (n == "Friday"):
        return(5)
    elif (n == "Saturday"):
        return(6)
    else: return(None)


test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
test(day_num("Halloween") == None)

import math

def day_add(a,b):
    temp1 = day_num(a)
    temp1 = temp1 + b
    temp1 = temp1%7
    temp2 = day_name(temp1)
    return(temp2)

test(day_add("Monday", 4) ==  "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")


test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
