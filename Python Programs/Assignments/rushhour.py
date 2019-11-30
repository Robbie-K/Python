# robert Karg - 10145986
# Assignment 4: rushhour game - (text version)
import sys # used for the argv function

# my class for the text version
class CarGame:

    # function for handling the .txt data
    # and setting up other variables/lists to be used later on
    @classmethod
    def dataSetup(cls):
        textFile = open(sys.argv[1], 'r')
        textLines = [line.strip('\n') for line in textFile]
        textFile.close()
        textLines = [index.split(',') for index in textLines]
        cls.data = textLines
        cls.numCars = len(cls.data)
        cls.carNum = 1
        cls.list1 = [0, 0, 0, 0, 0, 0]
        cls.list2 = [0, 0, 0, 0, 0, 0]
        cls.list3 = [0, 0, 0, 0, 0, 0]
        cls.list4 = [0, 0, 0, 0, 0, 0]
        cls.list5 = [0, 0, 0, 0, 0, 0]
        cls.list6 = [0, 0, 0, 0, 0, 0]
        cls.tracker = -1
        cls.carNumList = []

    # the constructor uses the data to assign self all of its attributes
    def __init__(self):
        # this if prevents from making useless objects
        if CarGame.carNum == CarGame.numCars + 1:
            return
        self.orient = CarGame.data[CarGame.carNum - 1][0]
        self.carLength = int(CarGame.data[CarGame.carNum - 1][1])
        self.row = int(CarGame.data[CarGame.carNum - 1][2])
        self.column = int(CarGame.data[CarGame.carNum - 1][3])
        self.car = CarGame.carNum
        CarGame.carNumList.append(self) # list of all objects
        CarGame.carNum += 1



    # tbis function adds to the three parameter lists
    def addCarValues(self, list1, list2, list3):
        orient, column, car, carLength = self.orient, self.column, self.car, self.carLength
        if orient == 'h':
            for i in range(carLength):
                list1[column + i] = car
        else:
            list1[column] = car
            list2[column] = car
            if carLength == 3:
                list3[column] = car


    # this function uses addCarValues for each row to finish the grid
    @classmethod
    def addCar(cls, self):
        row = self.row
        if row == 0:
            # print(self.lists)
            self.addCarValues(cls.list1, cls.list2, cls.list3)
        elif row == 1:
            # print(self.lists)
            self.addCarValues(cls.list2, cls.list3, cls.list4)
        elif row == 2:
            # print(self.lists)
            self.addCarValues(cls.list3, cls.list4, cls.list5)
        elif row == 3:
            # print(self.lists)
            self.addCarValues(cls.list4, cls.list5, cls.list6)
        elif row == 4:
            # print(self.lists)
            self.addCarValues(cls.list5, cls.list6, None)
        else:
            # print(self.lists)
            print('')
            self.addCarValues(cls.list6, None, None)

    # simply creates the grid with all 6 lists(rows)
    @classmethod
    def createGrid(cls):
        grid = [cls.list1, cls.list2, cls.list3, cls.list4, cls.list5, cls.list6]
        cls.grid = grid

    # prints the board each time
    @classmethod
    def printState(cls):
        cls.tracker += 1
        for i in range(len(cls.grid)):
            print(cls.grid[i])
        if cls.tracker == 0:
            pass
        else:
            print('You have made %d moves.\n' %(cls.tracker))

    # has the player pick the car to move then calls to checkCar to check it
    @staticmethod
    def getMove():
        numCars = CarGame.numCars
        car = input("Please choose a car to move(1-%d): "%(numCars))
        carIsInt = False
        while carIsInt == False:
            try:
                car = int(car)
                while car < 1 or car > numCars:
                    car = input("Between 1 and %d only please! Choose again: " % numCars)
                    try:
                        car = int(car)
                        break
                    except None:
                        pass
                carIsInt = True
                continue
            except (ValueError, TypeError):
                car = input("Please pick a car to move(1-%d): " % numCars)
        carNum = CarGame.carNumList[car-1]
        carNum.checkCar()

    # checks if the car can move and if it can gets the direction, it also checks
    # if the car can move that direction, switches to the other if it can't and
    # then calls checkMoves(H or V) to check that respective direction
    def checkCar(self):
        car, grid, row, column, carLength = self.car, self.grid, self.row, self.column, self.carLength
        noMove = 'This car has no where to go... Choose again!' # more eficient
        if self.orient == 'h':
            if (car == grid[row][0] and grid[row][column + carLength] != 0):
                print(noMove)
            elif (car == grid[row][5] and grid[row][column - 1] != 0):
                print(noMove)
            elif  (grid[row][column - 1] != 0 and grid[row][column + carLength] != 0):
                print(noMove)
            else:
                direction = input("Move to the left(l) or right(r)? ")
                while direction != 'l' and direction != 'r':
                    direction = input("Try again! Type l or r: ")
                self.checkMovesH(direction)
        else:
            if (car == grid[0][column] and grid[row + carLength][column] != 0):
                print(noMove)
            elif (car == grid[5][column] and grid[row - 1][column] != 0):
                print(noMove)
            elif (grid[row - 1][column] != 0 and grid[row + carLength][column] != 0):
                print(noMove)
            else:
                direction = input("Move up(u) or down(d)? ")
                while direction != 'u' and direction !=  'd':
                    direction = input("Try again! Type u or d: ")
                self.checkMovesV(direction)

    # the vertical checking function which calls to moveCar at the end using
    # the direction and number of available spaces to move as parameters
    def checkMovesV(self, direction):
        car, grid, row, column, carLength = self.car, self.grid, self.row, self.column, self.carLength
        loop = True
        while loop == True:
            if direction == 'u':
                if (car == grid[0][column] or grid[row - 1][column] != 0):
                    print("This car can't move up! Switching to down..")
                    direction = 'd'
                    continue
                else:
                    count = 0
                    for i in range(row - 1, -1, -1):
                        if grid[i][column] == 0:
                            count +=1
                        else:
                            break
            else:
                if ( car == grid[-1][column] or grid[row + carLength][column] != 0):
                    print("This car can't move down! Switching to up..")
                    direction = 'u'
                    continue
                else:
                    count = 0
                    for i in range(row + carLength, 6, 1):
                        if grid[i][column] == 0:
                            count += 1
                        else:
                            break
            loop = False
        self.moveCar(direction, count)

    # checking horizontal function, does the same thing as the vertical check moves function
    def checkMovesH(self, direction):
        car, grid, row, column, carLength = self.car, self.grid, self.row, self.column, self.carLength
        loop = True
        while loop == True:
            if direction == 'l':
                if (car == grid[row][0] or grid[row][column - 1] != 0):
                    print("This car can't move left! Switching to right..")
                    direction = 'r'
                    continue
                else:
                    count = 0
                    for i in range(column - 1, -1, -1):
                        if grid[row][i] == 0:
                            count += 1
                        else:
                            break
            else:
                if (car == grid[row][-1] or grid[row][column + carLength] != 0):
                    print("This car can't move right! Switching to left..")
                    direction = 'l'
                    continue
                else:
                    count = 0
                    for i in range(column + carLength, 6, 1):
                        if grid[row][i] == 0:
                            count += 1
                        else:
                            break
            loop = False
        self.moveCar(direction, count)

    # updates the grid based on the move picked by the player
    # then calls to the printState function to print the board
    def moveCar(self, direction, count):
        car, grid, row, column, carLength = self.car, self.grid, self.row, self.column, self.carLength
        move = input(
            "That car can move up to %d space(s). How many would you like to move: " % count)
        moveIsInt = False
        while moveIsInt == False:
            try:
                move = int(move)
                while move < 1 or move > count:
                    move = input("Between 1 and %d only please! Choose again: " % count)
                    continue
                moveIsInt = True
                continue
            except:
                print("Please enter a number!")
                move = input("Please pick how many spaces to move(1-%d): " % count)
        # updating the board
        for i in range(1, move + 1, 1):
            if direction == 'l':
                grid[row][column - 1] = car
                grid[row][column + carLength -1] = 0
                column -= 1
                self.column -= 1
            elif direction == 'r':
                grid[row][column + carLength] = car
                grid[row][column] = 0
                column +=1
                self.column += 1
            elif direction == 'u':
                grid[row - 1][column] = car
                grid[row + carLength - 1][column] = 0
                row -= 1
                self.row -= 1
            else:
                grid[row + carLength][column] = car
                grid[row][column] = 0
                row += 1
                self.row += 1
        CarGame.printState()

    # simply checks the status of  the game and ends it if the player has won
    @classmethod
    def checkWinner(cls):
        if cls.grid[2][5] == 1:
            print("\nCongrats you won!\nYou won in %d moves!" %(cls.tracker))
            print()
            return True
        else:
            return False

# main function puts everything together to run the game
def main():
    CarGame.dataSetup()
    # setting up 13 cars so that my function can run with every .txt file
    car1, car2, car3, car4, car5 = CarGame(), CarGame(), CarGame(), CarGame(), CarGame()
    car6, car7, car8, car9, car10 = CarGame(), CarGame(), CarGame(), CarGame(), CarGame()
    car11, car12, car13 = CarGame(), CarGame(), CarGame()

    # adding cars to the grid one at a time
    for i in range(CarGame.numCars):
        CarGame.addCar(CarGame.carNumList[i])
    CarGame.createGrid()
    # this allows me to import this file for my pygame file without it starting
    # the text version
    if __name__ == '__main__':
        CarGame.printState()
        winner = False
        while winner == False:
            CarGame.getMove()
            winner = CarGame.checkWinner()



main()
