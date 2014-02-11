## This function counts the highest number of occurrences of a character in a word.

def countChar(word):
	new = word.lower()
	dic = {}
	for i in new:
		if i not in dic:
			dic[i] =1
		else:
			dic[i] += 1
	return max(dic.values())

print countChar("hellojldjvl;kzjvlzxkjv")

def wowCount(string):
	return max( string.count(char) for char in set(string) )

print set("hello")
print wowCount("toffeee kup")

# def parseword(a_word):
# 	a_word=a_word.lower()
# 	# count=list(map(a_word.count, a_word))
# 	count = []

# 	return (max(count))
# print parseword("hello")