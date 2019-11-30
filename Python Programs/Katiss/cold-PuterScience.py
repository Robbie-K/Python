# 1 input n on first line that lets us know the number of days
# second line is the data for n days
# determine how many days Chicago was below 0

numDays = int(input())
days = input()
daysList = days.split(" ")
count = 0
for i in range (numDays):
    if int(daysList[i]) < 0:
        count += 1

print(count)
