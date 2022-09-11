def ReverseList(A):
	stack = []
	for i in A:
		stack.append(i)
	pos = 0
	while len(stack) > 0:
		A[pos] = stack.pop()
		pos += 1
	return A

test_data = [10, -4, -1, 20, 13, -3]
print(ReverseList(test_data))
