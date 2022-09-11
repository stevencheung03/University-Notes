def FindMinimum(givenlist):
	if len(givenlist) == 1:
		return givenlist[0]
	else:
		return min(givenlist[0], FindMinimum(givenlist[1:]))


examplelist = [1,0,3,-34]

print(FindMinimum(examplelist))