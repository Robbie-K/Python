def factorialFor(n):
    temp = 1
    for i in range (n,0,-1):
        temp = i * temp   #not working
        return(temp)

print(factorialFor(3))
