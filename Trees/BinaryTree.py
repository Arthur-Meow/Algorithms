class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tempTree = BinaryTree(newNode)
            tempTree.leftChild = self.leftChild
            self.leftChild = tempTree

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tempTree = BinaryTree(newNode)
            tempTree.rightChild = self.rightChild
            self.rightChild = tempTree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key