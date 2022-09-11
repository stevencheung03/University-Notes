def InsertionSort(A):
	for i in range(1, len(A)):
		temp = A[i]
		j = i-1
		while j >= 0 and temp < A[j]:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = temp
		print(A)

test_data = [1,17,7,20,4,8,9,13,-2]
InsertionSort(test_data)
