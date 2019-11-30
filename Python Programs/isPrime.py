def isPrime(num):
    for i in range(2,num+1,1):
        for j in range(2,10):
            if i == j:
                continue
            if i % j == 0:
                print(i, "NOT Prime")
                if i == num:
                    return True
                break
            elif j == 9:
                print(i, "Is Prime")
                if i == num:
                    return False


def main():
    n = int(input("Enter a number to check for prime numbers up to and including: "))
    isPrime(n)

main()
