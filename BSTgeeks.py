class Node:

    # Constructor to create a new node
    def __init__(self, key,name):
        self.key = key
        self.left = None
        self.right = None
        self.name=name


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,root.name)
        inorder(root.right)
# A utility function to insert a
# new node with given key in BST
def insert(node, key,name):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key,name)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key,name)
    else:
        node.right = insert(node.right, key,name)

    # return the (unchanged) node pointer
    return node


# Given a non-empty binary
# search tree, return the node
# with minum key value 
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key,name):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key <= root.key and root.name!=name:
        root.left = deleteNode(root.left, key,name)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (key > root.key) and root.name!=name:
        root.right = deleteNode(root.right, key,name)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        if name==root.name and root.key==key:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
            root.key = temp.key
            root.name=temp.name



        # Delete the inorder successor
            root.right = deleteNode(root.right,temp.key,temp.name)
	    #root.right=None

    return root


# Driver code
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """

root = None
root = insert(root, 50,"a")
root = insert(root, 30,"b")
root = insert(root, 30,"h")
root = insert(root, 50,"o")
root = insert(root, 20,"c")
root = insert(root, 40,"d")
root = insert(root, 70,"e")
root = insert(root, 60,"f")
root = insert(root, 80,"g")
root=insert(root,30,"yo")


print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20,"c")
inorder(root)
print("\nDelete 30")
root = deleteNode(root, 30,"b")

inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50,"a")
print("Inorder traversal of the modified tree")
inorder(root)
root = deleteNode(root, 30,"h")
print("Inorder traversal of the modified tree")
inorder(root)
root = deleteNode(root, 30,"yo")
print("Inorder traversal of the modified tree")
inorder(root)
print("bdfkbksdbk")
root = insert(root, 30,"k")
print(root.name)
inorder(root)
