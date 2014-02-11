#McNuggets problem

def buyNug(n):
	if n < 0:
		return False
	if n%20 == 0:
		return True
	if n>3 and n%3 == 0:
		return True
	if n<20:
		return False
	else:
		return buyNug(n-20)
print buyNug(0)