# formula for triangular numbers is: 1+2+3....n=((n(n+1))/2)
# start i and temp 1 from 0 so that entry 0 is 1 and 1 is 3, etc.
def print_triangular_numbers(n):
    temp1 = 1
    for i in range(1,n+1,1):
        temp1 = temp1 + 1
        temp2 = (i*(i+1))/2
        print ("%-7d %.f" %(i,(temp1 + temp2)))     # use %-7d to print 7 spaces after i
        # "%.f" rounds the number to the closest integer (in this case just removes .0)

    return


def num_digits(n):
    count = 0
    if n == 0:      # added an if statement to return 1 given num_digits(0)
        count = 1
    if n <0:    # added this if statement to change the value of n to positive
        n = -n  # if it is negative and then keep going
    while n != 0:
        count = count + 1
        n = n // 10

    return count


# Maryam said I could leave these in here and not lose marks
# test function from the book, changed slightly to make more sense to me
import sys
def test(did_pass):
    """  Print the result of a test.  """
    lineNum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        message = "Test at line {0} ok".format(lineNum)
    else:
        message = ("Test at line {0} FAILED.".format(lineNum))
    print(message)


def test_suite():
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
