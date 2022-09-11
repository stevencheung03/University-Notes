def SelectionSort(A):
	for i in range(len(A)):
		min = i
		for j in range(i+1, len(A)):
			if A[min] > A[j]:
				min = j   
		A[i], A[min] = A[min], A[i]
	return A

test_data = [10, -4, -1, 20, 13, -3]
print(SelectionSort(test_data))
