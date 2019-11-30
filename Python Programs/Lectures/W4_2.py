
def multiplicationTable():
	for i in range(1,10):
		row = ""
		for j in range(1,10):
			row += str(i*j) + " "
			print(row)

def christmasTree():
	h = int(input("How tall would you like the tree? "))

	for i in range(h):
		row = ""
		for j in range(h-i-1):
			row += " "
		for j in range(2*i+1):
			row += "*"
		print(row)





#what we did in class:
# h = 5
# for i in range(h):
# 	row = ""
# 	for j in range(h-i-1):
# 		row += " "
# 	for j in range(2*i+1):
# 		row += "*"
# 	print(row)
