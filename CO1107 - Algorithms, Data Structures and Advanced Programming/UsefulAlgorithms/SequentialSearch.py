def SequentialSearch(A, target):
	for i in A:
		if target == i:
			return target + " is in the list!"
