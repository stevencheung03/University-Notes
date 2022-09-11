def Factorial(number):
    if number == 1:
        return number
    else:
        return number*Factorial(number-1)

result = []

GivenNumber = int(input("Enter a positive integer: "))

for i in range(1,GivenNumber+1):
	result.append(Factorial(i))

print(result)