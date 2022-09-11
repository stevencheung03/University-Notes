def ConvertToList():
	# filename = str(input("Enter the file name: "))
	# fullfilename = filename + ".txt"

	line_count = 0

	with open("tiny.txt") as file:
		for line in file:
			if line != "\n":
				line_count += 1
	ResultingList = []
	with open("tiny.txt") as file:
		for i in range(0, line_count):
			data = file.readlines()
			ResultingList.append(data)
			for j in ResultingList:
				for k in range(0,1):
					if k == 0:
						ResultingList[i][k] = ResultingList[i][k] + "miles"
					else:
						ResultingList[i][k] = "£" + ResultingList[i][k]
	return ResultingList

print(ConvertToList())