def selectionSortPrice ( array,col ):
    vendor = len( array )
    for position in range(vendor-1):
        minRow = position
        for temp in range( position + 1 , vendor ):
            if array [temp ] [ col ] < array [minRow ] [ col ] :
                minRow = temp
        array [ position ] , array [minRow] = array [minRow] , array [ position ]

    return array

def selectionSortDistance ( array, col ):
    vendor = len( array )
    for position in range(vendor-1):
        minRow = position
        for temp in range( position + 1 , vendor ):
            if array [temp ] [ col ] < array [minRow ] [ col ] :
                minRow = temp
        array [ position ] , array [minRow] = array [minRow] , array [ position ]

    return array

def printList(distCost):
    for pair in distCost:
        stringFormatted = str (pair[0])+" Miles, "+"£ "+str (pair [1])
        print(stringFormatted)

fileName = input("Enter a file name: ")
infline = open( fileName )
table = []
recNum = 0
for line in infline :
    table.append(line.split(','))
    table[recNum][0]=int(table[recNum][0])
    table[recNum][1]=float(table[recNum][1])
    recNum+=1

infline.close()
userChoice=""
while not userChoice == 4 :
    userChoice = int(input("Enter choice (1): Print / (2): Sort on Distance / (3): Sort on price / (4):Quit : "))
    if userChoice==1 :
        printList (table)
    elif userChoice== 2:
        printList(selectionSortDistance(table ,0))
    elif userChoice==3 :
        printList(selectionSortPrice( table ,1))
    elif userChoice==4 :
        print("Quitting . . . ")
    else : print("Invalid input")

