def subsetOf (L,M) :
    bitList= [ 0 ] * len(L)
    for index in range ( len(L ) ) :
        for item in M:
            if L[ index ] == item :
                bitList[ index ] = 1
    return bitList
L=[2,17,12,5,66,20,7]
M=[2,12,66]
print(subsetOf(L,M))
