# function to replace "old" letters in the string "s" with "new" letters
def replace(s, old, new):
    s = s.replace(old,new)  # simply use replace and all instances of the input old
                            # become the input "new" in the inputed string "s"
    return s




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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

# test_suite()
