# function to return the original word followed by the word backwards
# effectively mirroring the word given
def mirror(word):
    mirrorWord = word    # set this up to add the mirrorletters to the original word in the for loop
    for i in range(len(word)-1,-1,-1): # negative range to start from the back of the word and work to the front
        mirrorLetter = word[i]         # the letters used to add to the intitial word
        mirrorWord += mirrorLetter     # adding the letters one by one onto the back of the original word
    return(mirrorWord)

# function to take a letter and word as input respectively and return the word without any
# instances of the letter
def remove_letter(letter, word):
    newWord = word.replace(letter, "") # replace every instance of the letter with nothing aka delete every instance of the letter
    return(newWord)


# used for testing my functions:
import sys
def test(did_pass):
    """  Print the result of a test.  """
    lineNum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        message = "Test at line {0} passed".format(lineNum)
    else:
        message = ("Test at line {0} FAILED.".format(lineNum))
    print(message)

# test cases suggested from the questions used in the test suite:
def test_suite():
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
