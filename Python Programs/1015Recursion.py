def fibb(n):
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    return(fibb(n-1)+fibb(n-2))
x = int(input("enter number"))
x = fibb(x)
print(x)
