def compress(string):
  """
	return the string in chr-number of chr format if it's shorter than the original string.
	e.g. "helloooo" will become "h1e1l2o4", but "helo" is stil "helo" 
	"""
	result = ""
	i = 0
	strLen = len(string)
	while i < (strLen-1):
		count = 1
		while string[i] == string[i+1]:
			count += 1
			i = i+1
		result = result + string[i] + str(count)
		i = i+1
		if len(result) > strLen:
			return string
	return result

string = "hello"
print compress(string)
