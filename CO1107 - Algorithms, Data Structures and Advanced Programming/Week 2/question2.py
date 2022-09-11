def SelectionSort(array):
	unsortedarray = array
	for i in range(len(unsortedarray)):
		min_idx = i
		for j in range(i+1, len(unsortedarray)):
			if unsortedarray[min_idx] > unsortedarray[j]:
				min_idx = j
				
		unsortedarray[i], unsortedarray[min_idx] = unsortedarray[min_idx], unsortedarray[i]
	
	return unsortedarray