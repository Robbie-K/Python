#Assigning all of the variables

P = 10000       #principal
n = 12          #times interest is compounded
r = 8/100       #interest rate(8%)/100 for the equation

#Rretreiving the years t from user

t = int(input("How many years will the interest be compounded for?: "))

#Evaluating for A (the final amount)

A = P * ( 1 + (r / n))**(n * t)

#displaying the final result

print("The final amount will be:", A,"$")
