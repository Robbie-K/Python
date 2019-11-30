# Robert Karg exercise 7
# function to "flatten" aka get rid of all the [] inside of a list
def flatten(numList):
    newList = [] # creating two lists to be used later
    finalList = []
    indexNum = 0 # used to find the place of index
    # this if statement just checks if the list is empty then returns it if it is
    if numList == []:
        return(numList)
    # for loop that checks every index in numList for inner lists
    for index in numList:
        if isinstance(index, list) == True: # if there are inner lists
            # this appends every index of the inner index to the newList
            for i in range(len(index)):
                newList.append(numList[indexNum][i])
        else: # when index isn't a list
            # this appends the index-indexNum in numList to the newList
            newList.append(numList[indexNum])
        indexNum +=1 # to keep track of the index being used
    innerLists = True # condtion for the while loop
    while innerLists == True:
        for index in newList:
            if isinstance(index,list) == True: # checking for lists in the list
                tempList = flatten(newList) # use the function to flatten the newList
                # then this appends each index of tempList into the empty list: finalList
                for i in range(len(tempList)):
                    finalList.append(tempList[i])
            else:
                innerLists = False # ends the loop if there are no more inner loops
                continue # skips the rest of the loop and ends it
            return(finalList)
            # if there were twice nested lists using recursion will get rid of them since
            # the while loop runs until innerLists = False, aka line 23 is false
            # recursion will happen with each new-newList until there are no more lists in the list
            # then whichever iteration ran last returns the current finalList
    return(newList)
    # if there are no lists in the list after the first for loop the list only
    # had single nested lists so newList is the correct list


# just the test function from the text, modified slightly to make more sense to me
import sys
def test(did_pass):
    """  Print the result of a test.  """
    lineNum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        message = "Test at line {0} passed".format(lineNum)
    else:
        message = ("Test at line {0} FAILED.".format(lineNum))
    print(message)

# test cases suggested from the question used in the test suite:
def test_suite():
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
                  ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])


# test_suite()
