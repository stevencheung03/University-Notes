def duplicate(listA,listB):
    aPos = 0
    bPos = 0
    dupes = []
    while aPos < len(listA) and bPos < len(listB):
        aVal = listA[aPos]
        bVal = listB[bPos]
        if aVal == bVal:
            dupes.append(aVal)
            aPos+=1
            bPos+=1
        elif aVal < bVal:
            aPos +=1
        else:
            bPos +=1
    return dupes

listA=[1,2,3,4,5]
listB=[1,2,5,6,7]
print(duplicate(listA,listB))
