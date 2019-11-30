def textRemover(s):
    word = s
    for i in range(len(s)):
        if word[i] == "(":
            first = i
        elif word[i] == ")":
            last = i

    if first == 0:
        newWord = word[last+1:len(s)]
    else:
        newWord = word[0:first]+word[last+1:len(s)]



    print(newWord)
textRemover("The falling leaves drift by the window (the autumn leaves of red and gold)")
textRemover("(403) 233 - 8733")
textRemover("aBc(233) D e")
