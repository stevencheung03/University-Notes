def recursiveSum ( aList ):
    return recSum( aList ,0)
def recSum( aList , pos ):
    if pos == len( aList ):
        return 0
    else :
        return aList [ pos ] + recSum( aList , pos+1)

a=[1,2,3,4,5]
print(recursiveSum(a))