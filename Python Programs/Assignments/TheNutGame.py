# Assignment 3 - The Game of Nuts
# Robert Karg
# 10145986
#################################
# i solved all three parts of the assignment

# Please note: I wssn't sure when you wanted hats printed so i highlighted the spots
# i have print(hats) and when they print them so you can find the one/ones you need

import random  # to be used later on
# this function starts the game and returns the number of nuts
# nuts will obviously be used all throughout the game
def beginGame():
    print("Welcome to the game of nuts!")
    nuts = int(input(("How many nuts are on the board initially (10-100)? ")))
    while nuts < 10 or nuts > 100:
        nuts = int(input(("Please choose a number between 10 and 100: ")))
        continue
    print("Options:\n Play against a friend (1)\n Play against the computer (2)")
    print(" Play against the trained computer (3)")
    return nuts

# this function asks the player which option they would like abd returns the number
# used to start the desiered mode
def gameMode():
    mode = int(input("Which option do you take (1-3)? "))
    print()
    while mode < 1 or mode > 3:
        mode = int(input("Please choose a number between 1 and 3: "))
        continue
    return mode

# the function which gets the players move and returns the remaining nuts
def playerMove(nuts,player):
    print("There are " "%d" " nuts on the board." %(nuts))
    move = int(input(player+": How many nuts do you take (1-3)? "))
    while move < 1 or move > 3:
        move = int(input(player+", please take either 1, 2 or 3 nuts only! "))
        continue
    nuts -= move # subtracting the nuts they took
    return nuts

# my player vs player function
def twoPlayer(nuts):
    game = True
    while game == True:
        # using my playerMove function so subtract the nuts then checking the
        # the nut count with my checkNutCount function
        nuts = playerMove(nuts,"Player 1")
        game = checkNutCount(nuts,"Player 1")
        print('') # just for line spacing
        # my checkNutCount function returns false if nuts <= 0
        # so the game will end if nuts are <=0
        if game == False:
            continue # continue ends the game right away
        # same as above but for player 2
        nuts = playerMove(nuts,"Player 2")
        game = checkNutCount(nuts, "Player 2")
        print('')

# my function for resting the game in player vs ai or player vs trained ai modes
def gameReset(player):
    newGame = int(input(player+", play again (1 = yes, 0 = no)? "))
    if newGame == 1:
        print('')
        return True # true continus the game
    else:
        return False # false ends the game

# this function creates the two lists i use for any ai and returns them
def initializeComputer(nuts):
    hats = []
    beside = []
    for i in range(nuts):
        hats.append([1,1,1]) # [1,1,1] since hats is just a count of 1s 2s or 3s
        beside.append([0,0,0])
    return hats, beside

# my function for the computer movement that returns remaining nuts
def computerMove(hats,beside,nuts,mode):
    rand = random.Random() # random object
    ones = int(hats[nuts-1][0])*str(1) # makes the count into that many 1s as a string
    twos = int(hats[nuts-1][1])*str(2) # same here for 2s
    threes = int(hats[nuts-1][2])*str(3) # and here for 3s
    # ex: if the hat is [2,4,3] choice will be '112222333'
    choice = ones + twos + threes
    ball = int(rand.choice(choice)) # then this takes a random number from choice
    if mode == 2: # so this doesnt print while trainedai runs 100000 times
        # these print what the ai does
        print("\nThere are " "%d" " nuts on the board." %(nuts))
        print("AI takes " "%d" " nuts.\n" %(ball))
    # this if-elif statement adds to the beside counter to be used later
    if ball == 1:
        beside[nuts-1][0] += 1
    elif ball == 2:
        beside[nuts-1][1] += 1
    else:
        beside[nuts-1][2] += 1

    nuts -= ball # subtracting how many nuts the computer takes
    return nuts

# my human against ai function to be used for both ai against human modes
def computer(nuts,mode):
    originalNuts = nuts # to be used if the player plays again

    if mode == 2: # human vs untrained ai makes two new lists
        hats, beside = initializeComputer(nuts)
    else: # human vs trained ai trains the ai and uses those lists
        print("Please wait while AI is trained...")
        hats, beside = trainAI(nuts) # trained ai lists
        mode = 2 # set back to 2 so the computerMove function prints the ai moves

    game = True # used for the loop
    while game == True:
        nuts = playerMove(nuts,"Player 1") # player 1 move
        check = checkNutCount(nuts,"Player 1") # checks the number of nuts
        # checks the nut count and runs the reset function
        # it updates the hats list for the ai each time as well
        if check == False:
            game = gameReset("Player 1")
            if game == True:
                nuts = originalNuts # reseting nuts for new game
            else: # this just updates the list before ending
                computerWin = True
                hats, beside = updateComputerHats(hats,beside,computerWin,originalNuts)
                continue
            computerWin = True
            hats, beside = updateComputerHats(hats,beside, computerWin,originalNuts)
            #############################################################
            # """ This prints at the end of each game if the ai wins""" #
            #print(hats)
            #############################################################
            continue

        nuts = computerMove(hats,beside,nuts,mode) # computer move
        check2 = checkNutCount(nuts,"AI") # checks the number of nuts
        # this if does the same thing as above
        if check2 == False:
            game = gameReset("Player 1")
            if game == True:
                nuts = originalNuts
            else:
                computerWin = False
                hats, beside = updateComputerHats(hats,beside,computerWin,originalNuts)
                continue
            computerWin = False
            hats, beside = updateComputerHats(hats,beside,computerWin,originalNuts)
            ##############################################################
            # """ This prints at the end of each game if player wins """ #
            #print(hats)
            ##############################################################

################################################################
# """ This prints when the player says no to playing again """ #
    # note its indented
    print(hats)

################################################################

# my function that puts beside into hats if the ai wins and removes beside if it loses
def updateComputerHats(hats,beside, computerWin,originalNuts):
    if computerWin == True: # if ai wins
        for i in range(len(hats)):
            for j in range(len(hats[i])):
                hats[i][j] += (beside[i][j]) # adding beside into hats
                # since i opted to not remove from hats each time, adding only one beside
                # accomplishes the same as adding 2 when you remove first
        beside = [] # resets beside
        for i in range(originalNuts):
            beside.append([0,0,0])
        return hats, beside
    else: # if ai loses
        for i in range(len(hats)):
            for j in range(len(hats[i])):
                if hats[i][j] >= 2: # >=2 makes sure hats will never contain zero
                    hats[i][j] -= (beside[i][j]) # subtracts every entry inside beside
                    # this works because beside is only ever 0 or 1
        beside = [] # resets beside
        for i in range(originalNuts):
            beside.append([0,0,0])
        return hats, beside # returns the altered hats and brand new beside lists


# this checks if nuts <= 0 and tells the player or ai they lost then ends (or resets) the game
# by returning False
def checkNutCount(nuts,player):
    if (nuts == 0 or nuts == -1 or nuts == -2):
        if player == "AI":
            print("AI loses.")
            return False
        else:
            print(player+", you lose.")
            return False
    else:
        return True


# this function trains the ai
def trainAI(nuts):
    rand = random.Random() # random object
    originalNuts = nuts # for reseting the game
    mode = 3 # to not print computers movement
    # the new lists for the ais
    hats2, beside2 = initializeComputer(nuts)
    hats, beside = initializeComputer(nuts)
    for i in range(100000): # running 100,000 games
        if nuts == originalNuts: # random first move
            nuts -= rand.randint(1,3)
        else:
            nuts = computerMove(hats2,beside2,nuts,mode) # ai2 move

        if nuts <= 0:
            aiWin = True # since ai won
            nuts = originalNuts # resets nuts
            # updates hats and resets beside for each ai
            hats, beside = updateComputerHats(hats,beside, aiWin,originalNuts)
            ai2Win = False # since ai2 lost
            hats2, beside2 = updateComputerHats(hats2,beside2,ai2Win,originalNuts)
            continue

        nuts = computerMove(hats, beside, nuts, mode) # ai move

        if nuts <= 0:
            aiWin = False # since ai lost
            nuts = originalNuts
            # same thing, updates hats and resets beside for each ai
            hats, beside = updateComputerHats(hats,beside, aiWin,originalNuts)
            ai2Win = True # since ai2 won
            hats2, beside2 = updateComputerHats(hats2,beside2,ai2Win,originalNuts)
            continue
    return hats, beside

# my main function where i call the other functions to run the game
def main():
    nuts = beginGame() # starts the game
    mode = gameMode() # gets the game mode
    # this if-elif-else runs the function corresponding to the mode
    if mode == 1:
        twoPlayer(nuts) # player vs player function
    elif mode == 2:
        computer(nuts,mode) # player vs ai function
    else:
        computer(nuts,mode) # same as above but it trains the ai since mode is 3


main() # running the game
