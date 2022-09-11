def mergeSort(givenlist):
    result = []  
    if len(givenlist) == 1:
        return givenlist  
    mid = len(givenlist) // 2

    sublist1 = mergeSort(givenlist[:mid])
    sublist2 = mergeSort(givenlist[mid:])

    x, y = 0, 0

    while x < len(sublist1) and y < len(sublist2):
        if sublist1[x] < sublist2[y]:
            result.append(sublist2[y])
            y = y + 1
        else:
            result.append(sublist1[x])
            x = x + 1

    result = result + sublist1[x:]
    result = result + sublist2[y:]

    return result

testlist=[3,2,4,1,5,9,7,6]
print(mergeSort(testlist))