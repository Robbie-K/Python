import sys


class RushHour:
    text = sys.argv[1]
    textFile = open(text, 'r')
    textLines = [line.strip('\n') for line in textFile]
    textFile.close()
    textLines = [index.split(',') for index in textLines]
    data = textLines
    numCars = len(data)
    dataList = []
    carNum = 1

    def __init__(self, data):
        self.carNum = RushHour.carNum
        carNum = self.carNum
        self.orient = data[carNum - 1][0]
        self.lengthCar = int(data[carNum - 1][1])
        self.row = int(data[carNum - 1][2])
        self.column = int(data[carNum - 1][3])
        RushHour.dataList.append([self.carNum, self.orient, self.lengthCar, self.row, self.column])
        RushHour.carNum += 1
        if RushHour.carNum == RushHour.numCars + 1:
            RushHour.carNum = 0

    @staticmethod
    def createGridLines():
        gridLine = []
        for i in range(6):
            gridLine.append(0)
        return gridLine

    @classmethod
    def setGrid(cls, dataList):
        print(dataList)
        line = RushHour.createGridLines()
        gridList0, gridList1, gridList2 = cls.createGridLines(), cls.createGridLines(), cls.createGridLines()
        gridList3, gridList4, gridList5 = cls.createGridLines(), cls.createGridLines(), cls.createGridLines()
        for i in range(len(dataList)):
            x, orient, lengthCar = dataList[i][0], dataList[i][1], dataList[i][2]
            row, column = dataList[i][3], dataList[i][4]
            print(x, orient, lengthCar, row, column)
            if row == 0:
                a, b, c = gridList0, gridList1, gridList2
                gridList0, gridList1, gridList2 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            elif row == 1:
                a, b, c = gridList1, gridList2, gridList3
                gridList1, gridList2, gridList3 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            elif row == 2:
                a, b, c = gridList2, gridList3, gridList4
                gridList2, gridList3, gridList4 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            elif row == 3:
                a, b, c = gridList3, gridList4, gridList5
                gridList3, gridList4, gridList5 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            elif row == 4:
                a, b, c = gridList4, gridList5, None
                gridList4, gridList5, tempNone0 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            else:
                a, b, c = gridList5, None, None
                gridList5, tempNone0, tempNone1 = cls.gridFiller(
                    a, b, c, orient, lengthCar, row, column, x)
            x += 1

        grid = []
        grid.append(gridList0)
        grid.append(gridList1)
        grid.append(gridList2)
        grid.append(gridList3)
        grid.append(gridList4)
        grid.append(gridList5)
        for i in range(len(grid)):
            print(grid[i])
        return grid

    @staticmethod
    def gridFiller(topList, middleList, bottomList, orient, lengthCar, row, column, x):
        rows = 6
        for i in range(rows):
            if row == i:
                if orient == 'h':
                    for j in range(lengthCar):
                        topList[column + j] += x
                else:
                    if lengthCar == 2:
                        topList[column] += x
                        middleList[column] += x
                    else:
                        topList[column] += x
                        middleList[column] += x
                        bottomList[column] += x
        return topList, middleList, bottomList


def getMove(car, column, row, grid, dataList):
    carOrient = dataList[car - 1][1]
    lengthCar = (dataList[car - 1][2])
    noMove = 'This car has no where to go... Choose again!'
    move = 0
    if carOrient == 'h':
        if (car == grid[row][0] and grid[row][column + lengthCar] > 0) or (grid[row][column - 1] != 0 and grid[row][column + lengthCar] != 0):
            print(noMove)
            move, direction = None, None
        else:
            direction = input("Move to the left(l) or right(r)? ")
            while direction != 'l' and direction != 'r':
                direction = input("Try again! Type l or r: ")
            while move == 0:
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
                                i = -1
                else:
                    if (car == grid[row][-1] or grid[row][column + lengthCar] != 0):
                        print("This car can't move right! Switching to left..")
                        direction = 'l'
                        continue
                    else:
                        count = 0
                        space = True
                        while space == True:
                            for i in range(column + lengthCar, 6, 1):
                                if space == False:
                                    continue
                                elif grid[row][i] == 0:
                                    count += 1
                                else:
                                    space = False
                if count == 1:
                    move = 1
                else:
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

    else:
        if (car == grid[0][column] and grid[row + lengthCar][column] > 0) or(grid[row - 1][column] != 0 and grid[row + lengthCar][column] != 0):
            print(noMove)
            move, direction = None, None
        else:
            direction = input("Move up or down? ")
            while direction != ('u' or 'd'):
                direction = input("Try again! Type u or d: ")

    return(move, direction)


def userMove(grid, dataList):
    tracker = 0
    while grid[2][5] != 1 and (grid[2][4] == 0 or grid[2][4] > 1):
        numCars = len(dataList)

        car = input("Please pick a car to move(1-%d): " % numCars)
        carIsInt = False
        while carIsInt == False:
            try:
                car = int(car)
                while car < 1 or car > numCars:
                    car = input("Between 1 and %d only please! Choose again: " % numCars)
                    continue
                carIsInt = True
                continue
            except print("Please enter a number!"):
                car = input("Please pick a car to move(1-%d): " % numCars)
        lengthCar = (dataList[car - 1][2])
        row = dataList[car - 1][3]
        if tracker == 0:
            column = dataList[car - 1][4]
        move, direction = getMove(car, column, row, grid, dataList)
        if move is None:
            continue
        for i in range(1, move + 1, 1):
            if lengthCar == 2:
                if direction == 'l':
                    grid[row][column - i] = car
                    grid[row][column + i] = 0
                    column -= 1
                elif direction == 'r':
                    grid[row][column + lengthCar] = car
                    grid[row][column] = 0
                    column += 1
                # """elif for up and else for down"""
            else:
                if direction == 'l':
                    grid[row][column - i] = car
                    grid[row][column + i + 1] = 0
                    column -= 1
                elif direction == 'r':
                    grid[row][column + lengthCar] = car
                    grid[row][column] = 0
                    column += 1
                # """elif for up and else for down"""
        for i in range(len(grid)):
            print(grid[i])
        tracker += 1


def main():
    data = RushHour.data
    car1, car2, car3 = RushHour(data), RushHour(data), RushHour(data)
    car4, car5, car6 = RushHour(data), RushHour(data), RushHour(data)
    car7, car8, car9 = RushHour(data), RushHour(data), RushHour(data)
    car10, car11, car12 = RushHour(data), RushHour(data), RushHour(data)
    car13, car14, car15 = RushHour(data), RushHour(data), RushHour(data)
    grid = RushHour.setGrid(RushHour.dataList)
    # data = getData()
    # dataList = checkData(data)
    # grid = setGrid(dataList)
    # userMove(grid, dataList)


main()
