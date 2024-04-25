class BinaryTree:
    def __init__(self, data):
        self.right = 0
        self.left = 0
        self.data = data
        
    def findDepth(node):
        if node is None:
            return 0
        else:
            leftDepth = BinaryTree.findDepth(node.left)
            rightDepth = BinaryTree.findDepth(node.right)       
            
            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
            
            
if __name__ == "__main__":
    obj = BinaryTree()
                
                   