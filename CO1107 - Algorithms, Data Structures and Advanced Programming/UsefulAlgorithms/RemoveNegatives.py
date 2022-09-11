def RemoveNegatives(A):
	for i in range(len(A)):
		item = A.pop(0)
		if item >= 0:
			A.append(item)
	return A

test_data = [10, -4, -1, 20, 13, -3]
print(RemoveNegatives(test_data))
