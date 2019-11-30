

def hasMatchingParenthesis(word):
    left = word.count('(')
    right = word.count(')')
    if left == right or (left == 0 and right == 0):
        print(True)
    else:
        print(False)
# hasMatchingParenthesis('(this should be tru)')
#
# hasMatchingParenthesis('this should ) not')
#
# hasMatchingParenthesis('this should too')
#
#
def elimSmallest(numList):
    minNum = numList[0]
    place = 0
    for i in range(len(numList)):
        if numList[i] < minNum:
            minNum = numList[i]
            place = i
    numList.remove(numList[place])
    print(numList)

elimSmallest([1,2,3,4,5)
