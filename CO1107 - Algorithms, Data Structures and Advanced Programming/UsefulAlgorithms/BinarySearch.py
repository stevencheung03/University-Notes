def binarySearch(aList, target):
	low = 0
	high = len(aList)-1
	while low <= high:
		mid = (low + high) // 2
		if aList[mid] == target:
			return mid
		elif aList[mid] > target:
			high = mid-1
		else:
			low = mid+1
	return -1
