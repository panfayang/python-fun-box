def inkyPinkyPonkey(N,K):
	assert (type(N) is int) and (type(K) is int) and N > 0 and K > 0
	children = []
	for i in range(N):
		children.append(i+1)
	temp = 0
	for i in range(N-1):
		num = (K+temp)%(N-i)-1
		print "Opps, number " + str(children.pop(num)) + " is out~"
		temp = num
	return "And number " + str(children.pop()) + " is the winner!"

print inkyPinkyPonkey(6,3)