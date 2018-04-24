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

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

t = BinaryTree(3)
t.insertLeftChild(2)
t.insertRightChild(5)

print(t.getRootVal())
print(t.getLeftChild().getRootVal())
print(t.getRightChild().getRootVal())


