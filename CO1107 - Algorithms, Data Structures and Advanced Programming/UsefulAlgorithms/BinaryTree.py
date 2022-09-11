class TreeNode:
	def __init__(self,item=None):
		self.item=item
		self.left=None
		self.right=None
    

class BinaryTree:
	def __init__(self, root):
		self.root=TreeNode(root)

	def __len__(self):
		return self.len_aux(self.root)
	def len_aux(self,current):
		if current is None:
			return 0
		else:
			return 1+self.len_aux(current.left)+self.len_aux(current.right)
	
	def sum_leaves(self):
		return self.sum_leaves_aux(self.root)
		
	def sum_leaves_aux(self,current):
		if current is None:
			return 0
		elif current.left is None and current.right is None:
			return current.item
		else:
			return self.sum_leaves_aux(current.left)+ self.sum_leaves_aux(current.right)
			
	def is_balanced(self):
		return self.height(self.root)
		
	def height(self,root):
		if root is None:
			return 0
		else:
			if (self.height(root.left) > self.height(root.right)):
				return (self.height(root.left) + 1)
			else:
				return (self.height(root.right) + 1)
		# if self.root is None:
		# 	return True    
		# 	LeftHeight = height(root.left)
		# 	RightHeight = height(root.right)
		# if ((LeftHeight - RightHeight) <= 1):
		# 	return True
		# else:
		# 	return False
            

ex=TreeNode(25)
bt=BinaryTree(ex)
bt.root.left=TreeNode(20)
bt.root.right=TreeNode(22)
bt.root.left.left=TreeNode(10)
bt.root.right.left=TreeNode(19)
bt.root.right.right=TreeNode(8)

print("The size of the binary tree is : ", bt.__len__())
print("The sum of the leaves is : ",bt.sum_leaves())
#print("",bt.mirror())
print(bt.is_balanced())
