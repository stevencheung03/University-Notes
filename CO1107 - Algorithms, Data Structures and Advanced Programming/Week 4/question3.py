def PrintToN(number):
	for i in range(1, number+1):
		print(i)

def PrintSquares(number):
	for j in range(1, number+1):
		print(j*j)

def GetSquares(number):
	SubResult = []
	for j in range(1, number+1):
		SubResult.append(j*j)
	return SubResult

def SumOfSquares(GivenList):
	if len(GivenList) == 1:
		return GivenList[0]
	else:
		return GivenList[0] + SumOfSquares(GivenList[1:])

GivenNumber = int(input("Enter a positive integer: "))

PrintToN(GivenNumber)
print("----------------")
PrintSquares(GivenNumber)
print("----------------")
print(SumOfSquares(GetSquares(GivenNumber)))
print("----------------")