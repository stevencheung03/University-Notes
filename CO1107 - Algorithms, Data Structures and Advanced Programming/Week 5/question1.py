def ReverseList(givenlist):
	result = []
	listlength = len(givenlist)
	while listlength > 0:
		result.append(givenlist[listlength-1])
		listlength -= 1
	return result

a = [1,2,3,4,5,6,7,8,9]
print(ReverseList(a))
