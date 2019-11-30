# given two inputs on seperate lines determines the qgraphical quadrant that point belongs to

x = eval(input())
y = eval(input())

if (x > 0 and y > 0):
    print(1)
elif (x < 0 and y > 0):
    print(2)
elif (x < 0 and y < 0):
    print(3)
elif (x > 0 and y < 0):
    print(4)
