### Temperarily add parent dir to Python path
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Stack import Stack
from BinaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    eTree = BinaryTree("")
    pStack = Stack()
    pStack.push(eTree)
    currentTree = eTree

    for x in fplist:
        if x == '(':
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif x not in '+-*/)':
            currentTree.setRootValue(eval(x))
            parentTree = pStack.pop()
            currentTree = parentTree
        elif x in '+-*/':
            currentTree.setRootValue(x)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif x == ')':
            parentTree = pStack.pop()
            currentTree = parentTree
        else:
            raise ValueError("Invalid symbol")

    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootValue()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootValue()

    