from re import search


class TreeNode():
	def __init__(self,item):
		self.item=item
		self.left=None
		self.right=None
    

class binarySearchTree():
	def __init__(self):
		self.root=None
    
    #add insert function here ....
	def insert(self,item):
		if self.root is None:
			self.root=TreeNode(item)
		else:
			self._insert(item,self.root)

	def _insert(self,item,currentNode):
		if item < currentNode.item:
			if currentNode.left is None:
				currentNode.left=TreeNode(item)
			else:
				self._insert(item,currentNode.left)
		elif item > currentNode.item:
			if currentNode.right is None:
				currentNode.right=TreeNode(item)
			else:
				self._insert(item,currentNode.right)
		else:
			print("Item is already existed in the tree")

	#  Task 2: Implement the search operation
	def search(self,tree, key):
		if (tree == None):
			return False
		if (tree.data == key):
			return True
		
		res1 = self.search(tree.left, key)
		
		if res1:
			return True
			
		res2 = self.search(tree.right, key)
		return res2

	#  Task 3: 
	def find_minimum(self, tree):
		current = tree
		
		while(current.left is not None):
			current = current.left
		return current.data

	#  Task 4:
	def treeRange(self, tree, a, b):
		result = search(tree, a) - search(tree, b)
		return result
        
	# Traversal algorithm, will be discussed next week
	def print_preorder(self):
		self._print_preorder_aux(self.root)
	def _print_preorder_aux(self,current):
		if current is not None:
			print(current.item)
			self._print_preorder_aux(current.left)
			self._print_preorder_aux(current.right)

            

bst=binarySearchTree()
bst.insert(24)
bst.insert(4)
bst.insert(3)
bst.insert(25)
bst.insert(13)
bst.insert(6)
bst.insert(45)
bst.insert(16)
bst.insert(67)
#print("The minimum item is : " ,bst.find_minimum())
bst.print_preorder()
#print(bst.treeRange(5,50))
