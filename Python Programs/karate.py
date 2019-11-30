def karate(floorSize):
    floorBlock = '_'

    for i in range(floorSize):
        for j in range(i+1, floorSize):
            fightFloor = floorBlock * floorSize
            fightFloor = placePlayer(fightFloor, i)
            fightFloor = placePlayer(fightFloor, j)
            if (checkRules(fightFloor)):
                print(fightFloor)

def placePlayer(floor, position):
    return (floor[:position] + '&' + floor[position+1:])

def checkRules(fightFloor):
    if fightFloor[0] == '&' or fightFloor[-1] == '&':
        return False
    split_str = fightFloor.split('&')
    for chunk in split_str:
        if len(chunk) <1:
            return False
        return True

karate(10)
