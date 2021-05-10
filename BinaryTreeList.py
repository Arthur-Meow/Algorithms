# Construct and operate binary tree using list

def binaryTree(root):
    # root is integer or list of lists
    return [root, [], []]

def insertLeft(root, newBranch):
    # 在根节点的左子树插入一个新列表,并且将原位置的列表变成新列表的左子树
    tempTree = root.pop(1)

    if len(tempTree) > 0:
        root.insert(1, [newBranch, tempTree, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root

def insertRight(root, newBranch):
    # 在根节点的右子树插入一个新列表,并且将原位置的列表变成新列表的右子树
    tempTree = root.pop(2)

    if len(tempTree) > 0:
        root.insert(2, [newBranch, [], tempTree])
    else:
        root.insert(2, [newBranch, [], []])
    
    return root

def getRootValue(root):
    return root[0]

def setRootValue(root, newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

