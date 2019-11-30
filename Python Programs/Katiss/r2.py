# S = (R1 + R2)/2 ---- R2 = 2*S - R1
line = input()
R1 = ""
S = ""
for i in range(len(line)):
    if line[i] == " ":
        for i in range(0,i): # i value finishes at i-1 (one before space)
            R1 += line[i]
        for i in range (i+2,len(line)): # have to start at i +2 (one after spcace)
            S += line[i]


R1 = int(R1)
S = int(S)
R2 = 2*S - R1
print(R2)
