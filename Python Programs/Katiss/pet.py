#Pet:

a1,a2,a3,a4 = input().split()  #splits the line into 4 inputs
a = 1
at = int(a1) + int(a2) + int(a3) + int(a4)

b1,b2,b3,b4 = input().split() #splits the second line into 4 inputs
b = 2
bt = int(b1) + int(b2)+int(b3)+int(b4)

c1,c2,c3,c4 = input().split() #splits the 3rd line into 4 inputs
c = 3
ct = int(c1)+int(c2)+int(c3)+int(c4)

d1,d2,d3,d4 = input().split() #4th
d= 4
dt = int(d1)+int(d2)+int(d3)+int(d4)

e1,e2,e3,e4 = input().split() #5th
e = 5
et = int(e1)+int(e2)+int(e3)+int(e4)

first = max(at, bt, ct, dt, et)  #assigns max to first for if

  if at == first: #prints the number of cook and their total score
    print(a, at)
elif bt == first:
    print(b, bt)
elif ct == first:
    print(c, ct)
elif dt == first:
  print(d, dt)
elif et == first:
  print(e, et)
