# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
root = Node('/')
root.left = Node('+')
root.right = Node('G')
root.left.left = Node('*')
root.left.right = Node('^')
root.left.left.left = Node('+')
root.left.left.left.left = Node('A')
root.left.left.left.right = Node('B')
root.left.left.right = Node('/')
root.left.left.right.left = Node('A')
root.left.left.right.right = Node('B')
root.left.right.left = Node('E')
root.left.right.right = Node('F')
print "Preorder traversal "
printPreorder(root)
print "\nInorder traversal "
printInorder(root)
print "\nPostorder traversal "
printPostorder(root)
