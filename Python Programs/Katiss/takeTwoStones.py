# Given N as input = number of stones
# and Alice and Bob consecutively each take 2 stones until
# there are none left
# if the remaining is odd Alice wins, otherwise Bob wins

# since they both always take two its simply the remainder of N/2
# aka N % 2 that tells us who wins:
N = eval(input())
if N % 2!= 0:
    print("Alice")
else:
    print("Bob")
