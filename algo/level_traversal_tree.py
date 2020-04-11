"""
Level order traversal of a tree is breadth first traversal for the tree.
There are basically two functions in this method. One is to print all nodes at a given level (printGivenLevel),
and other is to print level order traversal of the tree (printLevelorder).
printLevelorder makes use of printGivenLevel to print nodes at all levels one by one starting from root.
/*Function to print level order traversal of tree*/
printLevelorder(tree)
for d = 1 to height(tree)
   printGivenLevel(tree, d);

/*Function to print all nodes at a given level*/
printGivenLevel(tree, level)
if tree is NULL then return;
if level is 1, then
    print(tree->data);
else if level greater than 1, then
    printGivenLevel(tree->left, level-1);
    printGivenLevel(tree->right, level-1);
"""

# Recursive Python program for level order traversal of Binary Tree
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

# Function to  print level order traversal of tree
def PrintGivenLevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.data)
    elif level>1:
        PrintGivenLevel(root.left,level-1)
        PrintGivenLevel(root.right,level-1)

#Compute the height of a tree--the number of nodes along the longest path from the root node down to the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
        #compute height of  each tree
        lheight=height(node.left)
        rheight=height(node.right)
    return lheight+1 if lheight>rheight else rheight+1

def PrintLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        PrintGivenLevel(root,i)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

print("Level order traversal of binary tree is -")
PrintLevelOrder(root)

