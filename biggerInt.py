<<<<<<< HEAD
def biggerInt():
	number = raw_input("Please enter a positive integer")
=======
"""
Rearrange an integer's digits so it returns the largest number with same digits
"""

def biggerInt():
  number = raw_input("Please enter a positive integer")
>>>>>>> 7a82c4e6d661e63546863acfc3ab0bb7ce82d651
	
	while True:
		try:
			int(number)
			break
		except ValueError:
			number = raw_input("Please enter a positive integer")

	li = []
	final = ""
	for i in str(number):
		li.append(int(i))
	li.sort()
	for i in range(len(li)-1,-1,-1):
		final+=str(li[i])
	return final

<<<<<<< HEAD
print biggerInt()
=======
print biggerInt()
>>>>>>> 7a82c4e6d661e63546863acfc3ab0bb7ce82d651
