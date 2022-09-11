def listsum(GivenList):
	if len(GivenList) == 1:
		return GivenList[0]
	else:
		return GivenList[0] + listsum(GivenList[1:])

a = [1,4]

print(listsum(a))