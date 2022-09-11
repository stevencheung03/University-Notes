sequence = [1,2]

def incChange(N):
	if N > 1:
		print(int(incChange(N-1)) + int((incChange(N-3)-incChange(N-2)+1)))

incChange(5)

# (N-1)^2)/2 - (N/2) + 1