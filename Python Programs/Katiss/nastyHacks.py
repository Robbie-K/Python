# given a number of cases n
# followed by n times three inputs, r,e,c respectively for each case
# where r is revenue, e is expected revenue without advertising
# and c is the cost of advertising
# if r is higher than e-c it should print do not advertise
# if e-c is higher than r should print advertise
# if e-c = r then should print does not matter

n = int(input())
for i in range (n):
    numberList = input()
    List = numberList.split(" ")
    revenue = int(List[0])
    expectedRevenue = int(List[1])
    cost = int(List[2])
    if revenue > expectedRevenue - cost:
        print("do not advertise")
    elif expectedRevenue - cost > revenue:
        print("advertise")
    else:
        print("does not matter")
