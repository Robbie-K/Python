# question 7

def sortSequence(seqList):
    newList = []
    for i in range(len(seqList)-1):
        if seqList[i]<seqList[i+1]:
            newList.append(seqList[i])
            if seqList[i] == seqList[-2]:
                newList.append(seqList[i+1])
        else:
            if seqList[i]>seqList[i+1]:
                newList.append(seqList[i])
                break
    print(len(newList))


# sortSequence([1,3,5,7])

# question 5
#suggest doing it with count-sort
# def maxNum(num):
#     maxDig = num[0]
#     place = 0
#     for i in range(len(num)):
#         if maxDig < num[i]:
#             maxDig = num[i]
#             place = i
#
#     if place == 0



#question 1
# def pascalsTrig(n):
#     for i in range(n):
#         row

        # use the formula for combinations


#question 4
# given a matrix print the spiral of it
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for i in range(len(matrix)):
#     print(matrix[i])
#
# innerMatrix = []
# def spiralMatrix(matrix):
#     for i in range(len(matrix)):
#         innerMatrix.append(matrix[i][1:-1])
#     print(innerMatrix)
#     for i in range(len(matrix[0])):
#         print('%d,'%matrix[0][i],end ='')
#     for i in range(1,len(matrix)):
#         print('%d,'%matrix[i][-1],end ='')
#     bottomReverse = matrix[len(matrix)-1]
#     bottomReverse.reverse()
#     for i in range(1,len(bottomReverse)):
#         print('%d,'%bottomReverse[i],end ='')
#     for i in range(-1*len(matrix)+1,0,1):
#         print('%d,'%matrix[i][0],end ='')
#
# spiralMatrix(matrix)


#question 3
# look and say
def look_and_say(numList):
    newList= []
    class number:
        number = 0
        count = 0

        def __init__(self):
            self.number = self
            self.count = 1
        def addCount(self):
            self.count() +=1
        def countList(self):
            print(self,self.count())
            return (self)
    for i in range(len(numList)):

        if i == 0:
            numList[i] = number()
        else:
            if numList[i] in number():
                numList[i].addCount(index)
            else:
                numList[i] = number()



        for i in range(len(numList)):
            newList.append((numList[i]).countList())
        # if index in number():
        #     index.addCount(index)
    print(newList)
look_and_say([1,2,1,1,1,3,3,3])
