def primeNumbers():
    num = str(input("Which number would you like to check? "))
    length = len(num)
    for i in range(0,length,1) :
        numTemp = num[i]
        numTemp2 = str(numTemp + i)

    print(numTemp)




# def is_prime(num):   #in class solution
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"Is not a prime number")
#                 print(i,"times", num//i, "is",num)
#                 break
#             else:
#                 print(num, "Is a prime number")
#         else:
#             print(num,"is not a prime number")

def reverseString():
    userInput = str(input("Which word would you like reversed? "))
    n = len(userInput)
    for i in range(n-1,-1,-1):
        reverse = userInput[i]
        print(reverse, end='')    #end sets the start point for the next action

reverseString()
