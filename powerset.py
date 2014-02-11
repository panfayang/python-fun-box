def powerset(string):
	if len(string) == 0:
		return [""]
	elif len(string) == 1:
		return ["",string]
	else:
		temp = powerset(string[:-1])
		temp.extend(map(lambda x: x+string[-1], powerset(string[:-1])))
		return temp

print powerset("qwe")
##print map(lambda x: x+"qw"[-1], powerset("qw"[:-1]))
##print ['a'] + map(lambda x: x+"qw"[-1], powerset("qw"[:-1]))
