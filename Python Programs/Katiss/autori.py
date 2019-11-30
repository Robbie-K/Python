word = input()
initials = ""
for i in range (len(word)):
    if word[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        initials += word[i]

print(initials)
