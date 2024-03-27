class inorder:
	def __init__(self, v):
		self.root = v
		self.left = None
		self.right = None

def findInorder(node):
	if node is None:
		return "Null"

	findInorder(node.left)
	print(node.root, end=' ')
	findInorder(node.right)

if __name__ == '__main__':
	root = inorder(1)
	root.left = inorder(2)
	root.right = inorder(3)
	root.left.left = inorder(4)
	root.left.right = inorder(5)
	root.right.right = inorder(6)
	root.right.right.left = inorder(7)
 
	findInorder(root)
