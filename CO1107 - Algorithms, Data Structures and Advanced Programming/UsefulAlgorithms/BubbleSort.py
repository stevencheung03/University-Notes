def BubbleSort(A):
	n = len(A)
	for i in range(n-1):
		for j in range(n-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
	return A

test_data = [10, -4, -1, 20, 13, -3]
print(BubbleSort(test_data))
