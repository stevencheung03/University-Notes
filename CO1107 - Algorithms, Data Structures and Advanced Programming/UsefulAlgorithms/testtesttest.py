def count(i, S, target):
	list(map(str, S))
	result = []
	result_2 = []
	for i in range(len(S)):
		if S[i] == target:
			result.append(1)
		else:
			result.append(0)
	for j in range(len(result)):
		if result[j] == 1:
			result_2.append(1)
	return result_2

import numpy as np
def getMaximumEntry(list1):
	return np.max(list1)

def trylol(list1):
	x = 0
	y = 0
	maxElement = 0
	for i in range(4):
		for j in range(4):
			if (list1[i][j] > maxElement):
				maxElement = list1[i][j]
			y= j
		x = i
	return maxElement, i, j

aTable=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(getMaximumEntry(aTable))


S = "ab cbb ef b gh ijkl"
print(count(5, S, "b"))