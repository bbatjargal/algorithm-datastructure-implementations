class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, obj):
        if self.leftChild == None:
            self.leftChild = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, obj):
        if self.rightChild == None:
            self.rightChild = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

def preOrder_TreeTraversal(root):
    if root != None:
        print(root.key)
        preOrder_TreeTraversal(root.getLeftChild())
        preOrder_TreeTraversal(root.getRightChild())

def inOrder_TreeTraversal(root):
    if root != None:
        inOrder_TreeTraversal(root.getLeftChild())
        print(root.key)
        inOrder_TreeTraversal(root.getRightChild())

def postOrder_TreeTraversal(root):
    if root != None:
        postOrder_TreeTraversal(root.getLeftChild())
        postOrder_TreeTraversal(root.getRightChild())
        print(root.key)


b = BinaryTree(5)
b.insertLeftChild(4)
b.insertLeftChild(3)
b.insertLeftChild(2)
b.insertLeftChild(1)

b.insertRightChild(6)
b.insertRightChild(7)
b.insertRightChild(8)
b.insertRightChild(9)

print("PreOrder - Tree Traversal")
preOrder_TreeTraversal(b)

print("\n InOrder - Tree Traversal")
inOrder_TreeTraversal(b)

print("\n PostOrder - Tree Traversal")
postOrder_TreeTraversal(b)

