""" Robert Karg
Exercise 8 """

import sys

def countLettersInString(string):
    """ Function for counting letters in a given string and printing the results """
    letterCount = {} # empty dictionary

    # creates new keys if they don't exist, adds to them if they do
    for char in string:

        # checks if the char is a letter and ads it if it is
        if char not in letterCount:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                letterCount[char] = 1
            else:
                continue
        # ads to the count if the key already exists
        else:
            letterCount[char] +=1

    # this sorts the dictionary into alphabetical order
    letterCount = sorted(letterCount.items())

    # prints the results
    for key in letterCount:
        print('%-4s %d' %(key[0],key[1]))

# taking in the string with sys.stdin and running the function
string = (sys.stdin.readline()).lower()
countLettersInString(string)
