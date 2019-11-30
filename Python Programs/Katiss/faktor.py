#citations/articles = scientists
# citations = articles * scientists
# articles *(scientists-1) +1 = minimal scientists
# ex 38 * (24-1) + 1 = 875

userInput = input()
userList = userInput.split(" ")

articles = int(userList[0])
scientists = int(userList[1])

minScientists = (articles * (scientists-1)) + 1
if articles == 1:
    minScientists = scientists

print(minScientists)
