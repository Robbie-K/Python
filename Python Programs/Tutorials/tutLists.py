# tutorial exercises for lists

ls = ['apple',3,[10,20]]


lsInner = ls[2]
print(lsInner[0])

ls1 = ['Jim','Ken',2,'Hello']
ls2 = [2,3,4]

print(ls1+ls2)

print(ls[1:3])
print(ls[:3])
print(ls[3:])
print(ls[:])

newList = []
newList.extend(ls)
newList.reverse()

print(newList)
for i in range(len(newList)):
    x = newList[i]
    if type(x) == list:
        for j in range(len(x)):
            print(x[j])
        continue
    print(newList[i])
