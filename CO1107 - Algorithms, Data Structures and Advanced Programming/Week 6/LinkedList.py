from numpy import delete


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class linked_list:
	def __init__(self):
		self.head=None
		self.count=0

	def insertEnd(self, newNode):
		if self.head is None:
			self.head=newNode
			self.count += 1
		else:
			lastNode=self.head
			while True:
				if lastNode.next is None:
					break
				lastNode=lastNode.next
			lastNode.next=newNode
			self.count += 1


	def insertHead(self, newNode):
		tempNode = self.head
		self.head = newNode    
		self.count += 1
		self.head.next = tempNode


	def insertAt(self, newNode, position):
		currentNode=self.head
		currentPosition=0
		while True:
			if currentPosition == position:
				previousNode.next=newNode
				self.count += 1
				newNode.next=currentNode
				break
			previousNode=currentNode
			currentNode=currentNode.next
			currentPosition += 1


	def deleteEnd(self):
		lastNode=self.head
		while lastNode.next is not None:
			prevNode=lastNode
			lastNode=lastNode.next
		prevNode.next=None


	def deleteAt(self, position):
		currentNode=self.head
		currentPosition=0
		if linked_list.isEmpty() == False:
			while True:
				if currentPosition == position:
					prevNode.next=currentNode.next
					currentNode.next=None
					break
				prevNode=currentNode
				currentNode=currentNode.next
				currentPosition +=1
		else:
			return "Not enough nodes in this LinkedList.  :("
			
	
	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False
			
	
	def traversal(self):
		currentNode=self.head
		while currentNode is not None:
			print(currentNode.data)
			currentNode=currentNode.next
			
	
	def deleteHead(self):
		if self.isEmpty() is False:
			prevHead=self.head
			self.head=self.head.next
			prevHead.next=None
			print("The first item is deleted successfully")
		else:
			print("Linked List is empty, Delete Failed")

	
	def countNodes(self):
		return self.count

	
	def deleteAllNodes(self):
		while (self.head != None):
			temp = self.head
			self.head = self.head.next
			temp = None
		return "All nodes are deleted successfully."

	
	def delete_negatives(self):
		temp = self.head
		prev = None
		while temp is not None:
			if temp.data < 0:
				if temp == self.head:
					self.head = temp.next
					temp = self.head
				else:
					prev.next = temp.next
					temp = temp.next
			else:
				prev = temp
				temp = temp.next
		return "All negative nodes are deleted successfully."


	def sumAll(self):
		node = self.head
		result = 0
		while node is not None:
			result += node.data
			node = node.next
		return result


FirstNode=Node(12)
mylist=linked_list()
mylist.insertEnd(FirstNode)

SecondNode=Node(3)
mylist.insertEnd(SecondNode)

ThirdNode=Node(4)
mylist.insertEnd(ThirdNode)

FourthNode=Node(1)
mylist.insertHead(FourthNode)

NegativeNode=Node(-6)
mylist.insertEnd(NegativeNode)

mylist.deleteHead()
mylist.traversal()\

print(mylist.countNodes())

print(mylist.delete_negatives())

print(mylist.sumAll())

print(mylist.deleteAllNodes())
