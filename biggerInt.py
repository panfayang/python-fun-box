"""
Arrange an integer's digits so it returns the largest choice
"""

def biggerInt():
  number = raw_input("Please enter a positive integer")
	
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

print biggerInt()
