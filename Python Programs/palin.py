import math
string = input('Please enter the word to be checked. ')
mid = math.ceil(len(string)/2)
if len(string) == 1:
    numbers = '0123456789'
    if string not in numbers:
        print('This letter is a palindrome!')
    else:
        print('Invalid input!')
else:
    s = string.split(string[mid-1])
    for i in range(mid-1):
        x = s[1].find(string[i])
        if s[1][x] == string[i]:
            if i == mid -2 :
                print('This word is a palindrome!')
            continue
        else:
            print('This word is not a palindrome')
            break
