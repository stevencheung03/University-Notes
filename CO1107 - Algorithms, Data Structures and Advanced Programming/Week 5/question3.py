def FindMinimum(givenlist):
	if len(givenlist) == 1:
		return givenlist[0]
	else:
		return min(givenlist[0], FindMinimum(givenlist[1:]))

def minsort(insertlist):
	resultlist = []
	for i in range(0,len(insertlist)-1):
		resultlist.append(FindMinimum(insertlist))
		insertlist.remove(insertlist[i])
	return resultlist

print(minsort([4,3]))