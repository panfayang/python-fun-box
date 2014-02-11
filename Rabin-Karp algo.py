"""
This is a simple Rabin-Karp demo using 101 as the base of hash function
"""

class RabinKarp:
	def __init__(self,txtfile,searchword):
		txt = open(txtfile,'r')
		self.string = txt.read()
		# self.string = txtfile
		self.searchword = searchword
		# self.score = 0

	def hashFunction(self,substring):
		value = 0
		index = len(substring)-1
		for i in substring:
			value += ord(i)*(101**index)
			index = index-1
		return value

	def rollHash(self):
		length = len(self.searchword)
		constant = 101**(length-1)
		newDict = {}
		substring = self.string[0:length]
		score = self.hashFunction(substring)
		newDict[score] = [0]
		for i in range(0,len(self.string)-length):
			score = (score-(ord(self.string[i]))*constant)*101 + ord(self.string[i+length])
			if score not in newDict:
				newDict[score] = [i+1]
			else:
				newDict[score].append(i+1)

		return newDict

	def search(self):
		searchwordScore = self.hashFunction(self.searchword)
		dict = self.rollHash()
		if searchwordScore in dict:
			return dict[searchwordScore]
		else:
			return "not found."

rabin = RabinKarp("jane_eyre.txt","Rochester")
print len(rabin.search())
