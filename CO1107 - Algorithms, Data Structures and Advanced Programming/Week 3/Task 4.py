def largestInStack(aStack):
    
    #lets be sure to restore the stack to its original state afterwards
    backupStack = []
    if len(aStack)==0:
        return False #not possible to do this
    theMax = aStack.pop()
    backupStack.append(theMax) #put in backup

    while len(aStack)>0: #until empty
        item = aStack.pop()
        if item > theMax:
            theMax = item
        backupStack.append(item)

    while len(backupStack)>0: #until everything is back in aStack
        aStack.append(backupStack.pop())

    return theMax


#example usage
print(largestInStack([]))
print(largestInStack([1,5,7,89,3,1]))
print(largestInStack([9,8,6]))
print(largestInStack([1,9,8,16]))
