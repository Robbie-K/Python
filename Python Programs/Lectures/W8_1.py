# tuples

def test():
    sum1 = 0
    sum2 = 0
    for i in range(1,7,2):
        sum1 +=i
        sum2 -=i
    return sum1, sum2

def printSum():
    sum1, sum2 = test()
    print(sum1, sum2)

printSum()
