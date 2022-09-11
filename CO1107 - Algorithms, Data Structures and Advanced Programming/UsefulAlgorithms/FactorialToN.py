def factorialList (n):
    if n == 1:
        ansList = [0] * n
        ansList [0] = 1
    else :
        ansList = factorialList(n-1)
        ansList.append(n*ansList[n-2])
    return ansList

value=int (input("Enter the range: "))
print( factorialList ( value ))