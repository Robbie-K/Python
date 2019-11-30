# i wasnt sure if we needed a function so i created one anyway
def snakeCount():
    textFile = open('test.txt','r') # opens the file in read mode
    # creates a list with every line as a component of the list
    textLines = textFile.readlines() # creating a list with every line in it
    textFile.close # closes the file
    for i in range(len(textLines)):
        if textLines[i].count('snake') >= 1: # checking for the word snake on each line
            print(textLines[i]) # printing each line containing the word "snake"

snakeCount()
