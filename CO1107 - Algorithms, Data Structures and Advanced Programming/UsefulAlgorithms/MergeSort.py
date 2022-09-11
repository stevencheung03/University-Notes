def MergeSort(A):
	if len(A) > 1:
		mid = len(A)//2
		L = A[:mid]
		R = A[mid:]
		MergeSort(L)
		MergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			A[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			A[k] = R[j]
			j += 1
			k += 1
	return A

arr = [12, 11, 13, 5, 6, 7]
print(MergeSort(arr))
