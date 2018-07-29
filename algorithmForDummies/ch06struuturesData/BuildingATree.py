class binaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.nodeData)

tree = binaryTree("Root")
BranchA = binaryTree("Branch A")
BranchB = binaryTree("Branch B")

tree.left = BranchA
tree.right = BranchB

leafC = binaryTree("leaf C")
leafD = binaryTree("leaf D")
leafE = binaryTree("leaf E")
leafF = binaryTree("leaf F")

BranchA.left = leafC
BranchA.right = leafD
BranchB.left = leafE
BranchB.right = leafF

def traverse(tree):
    if tree.left != None:
        traverse(tree.left)
    if tree.right != None:
        traverse(tree.right)
    print(tree.nodeData)

traverse(tree)
