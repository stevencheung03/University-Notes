def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()


def ReverseList(stack):
	result = []
	stacklength = len(stack)
	for i in range(0, stacklength):
		push(result, pop(stack))
	return result


a = [1,2,3,4,5,6,7,8,9]
print(ReverseList(a))
