"""
Assumption: the first elements of the building info are in non-decreasing order

"""

def divideBlocks(rawData):
	"""
	rawData is a list of tuples, (x,y,z), where x is the x-axis point from the origin, y is the height, and z is the width.
	output: a list of lists of tuples, where buildings which are seperated are in different lists.
	"""
	divide = []
	temp = []
	farthest = rawData[0][0]+rawData[0][2]
	for building in rawData:
		further = building[0]+building[2]
		## If the buildings are apart
		if building[0]>farthest:
			divide.append(temp)
			temp = []
			temp.append(building)
			farthest = further
		## If the buildings are not apart
		else:
			temp.append(building)
			if further > farthest:
				farthest = further
	divide.append(temp)
	return divide

def listOfCoordinates(seperated):
	"""
	given a list of lists of 3-tuples, return a list of lists of (x,y), where the coordinates are
	"""
	CoorList = []
	temp = []
	for blocks in seperated:
		for building in blocks:
			temp.append((building[0],0))
			temp.append((building[0],building[1]))
			temp.append((building[0]+building[2],building[1]))
			temp.append((building[0]+building[2],0))
		CoorList.append(temp)
		temp = []
	return CoorList

def drawTwo(cor1, cor2):
	"""
	This function takes two coordinates and return the path in "xR, yU" or "xD,yR" or "xR" form
	"""
	x2 = cor2[0]
	y2 = cor2[1]
	x1 = cor1[0]
	y1 = cor1[1]
	words = str(x2-x1) + "R "
	if y2 > y1:
		words += str(y2-y1) + "U "
	elif y2 < y1:
		words += str(y1-y2) + "D "
	return words

def finalListOfCoordinates(listOfCoordinates):
	"""
	Input: a list of coordinates
	"""
	finalList = []
	start = (0,0)
	for block in listOfCoordinates:
		block.sort()
		finalList.append(block[0])
		temp = (,)
		for i in range(len(block)-1):
			if block[i+1][0] == block[i][0]:
				pass
			elif 
			else:
				finalList.append(block[i])
				temp = (block[i][0],0)
		finalList.append()


rawData1 = [(5,10,25),(10,20,15),(15,5,5)]
rawData2 = [(5,2,2),(10,2,1),(15,5,5)]

print listOfCoordinates(divideBlocks(rawData1))
print listOfCoordinates(divideBlocks(rawData2))


