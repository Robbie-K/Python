def hasMatchingParenthesis(word):
    left = word.count('(')
    right = word.count(')')
    if left == right or (left == 0 and right == 0):
        print(True)
    else:
        print(False)
hasMatchingParenthesis('(this should be tru)')

hasMatchingParenthesis('this should ) not')

hasMatchingParenthesis('this should too')
