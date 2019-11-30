# def countFor1(theString, theChar):
#     counter = 0
#     for ch in theString:
#         if (ch == theChar):
#             counter +=1
#     return counter
#
# def countFor2(theString, theChar):
#     counter = 0
#     for index in range(len(theString)):
#         if (theString[index] == theChar):
#             counter +=1
#     return counter
#
def movePlayers(floor):
    for i in range(1,len(floor),1):
        for j in range(1,len(floor),1):
            if floor[j] == "_":
                newFloor = (floor[:j]+"&"+floor[j+1:len(floor)])
                for h in range(j,len(floor),2):
                    if 
                    return(newFloor[:h+2]+"&"+newFloor[h+3:len(floor)])




def karatePlayers(n):
    floor = ""
    for i in range(n):
        floor += "_"






karatePlayers(8)
