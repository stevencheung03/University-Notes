def ShakerSort(A):
    no_swaps = True
    n = len(A)
    moving_right_start = 0
    moving_right_end = n-1
    moving_left_start = n-1
    moving_left_end = 0

    for j in range(n-1):
        if (j % 2 == 0):
            for i in range(moving_right_start , moving_right_end):
                if A[i] > A[i+1]:
                    no_swaps = False
                    A[i], A[i+1] = A[i+1], A[i]
            moving_left_start -= 1
            moving_right_end -= 1
        else:
            for i in range(moving_left_start , moving_left_end , -1):
                if A[i-1] > A[i]:
                    no_swaps = False
                    A[i], A[i-1] = A[i-1], A[i]
            moving_left_end += 1
            moving_right_start += 1
        if no_swaps:
            break
        no_swaps=True


a=[14,3,17,8,12,44,24]
ShakerSort(a)
print(a)
