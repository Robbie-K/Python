def reverseVowels():
    word = input("Please enter a word: ")
    vowels = 'aeiou'
    vowelList = []
    posList = []
    newList = []
    newWord = ''
    for i in range(len(word)):
        newList.append(word[i])
        for char in word[i]:
            if char in vowels:
                posList.append(i)
                vowelList.append(word[i])
    vowelList.reverse()
    for j in range(len(posList)-1,-1,-1):
        newList[posList[j]] = vowelList[j]
    for i in range(len(newList)):
        newWord += newList[i]
    print(newWord)


reverseVowels()
