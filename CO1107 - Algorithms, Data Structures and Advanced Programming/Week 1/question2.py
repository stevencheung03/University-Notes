from unittest import result


def GetProduct(text):
	InputSplit = list(text)

	ExtractedNumbers = []

	Result = 1
	
	for i in range(0, len(InputSplit)):
		ExtractedNumbers.append(InputSplit[i])
		if "*" in ExtractedNumbers:
			ExtractedNumbers.remove("*")

	ExtractedNumbers = list(map(int, ExtractedNumbers))

	for i in range(0, len(ExtractedNumbers)):
		Result *= ExtractedNumbers[i]

	return result

print(GetProduct("5*4"))