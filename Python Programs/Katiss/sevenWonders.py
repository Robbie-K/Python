line = input() 
t = line.count("T")  #counts the times T appears
c = line.count("C")
g = line.count("G")

tot_sum = (t)**2 + g**2 + c**2 + 7*(min(t, c, g))
print(tot_sum)
