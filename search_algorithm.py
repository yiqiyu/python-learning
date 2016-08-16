# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:37:00 2016

@author: Administrator
"""

import tree

def BinarySearch(array, target):
    high = len(array)-1
    low = 0
    while low <= high:
        mid = (low+high)/2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False


class Pointer(object):
    def __init__(self, side, node):
        self.side = side
        self.node = node
        
    def setValue(self, newNode):
        if self.side is "right":
            self.node.right = newNode
        elif self.side is "left":
            self.node.left = newNode


def findPointer(parent, target):
    """
    为target找到parent指向其的指针，返回从parent指向target的Pointer对象
    :param parent: target的直接父节点
    :param target: 目标节点
    """
    if parent.right is target:
        side = "right"  
    elif parent.left is target:
        side = "left"
    else:
        return False
    return Pointer(side, parent)


def SearchBST(TreeNode, key, parent=None):
    """
    二叉搜索树的查找操作，输入为树节点和关键字
    """
    if not TreeNode:
        print False
        return (None, parent)
    if TreeNode.data == key:
        print True
        return (TreeNode, parent)
    elif key < TreeNode.cargo:
        return SearchBST(TreeNode.left, key, TreeNode)
    elif key > TreeNode.cargo:
        return SearchBST(TreeNode.right, key, TreeNode)

        
def InsertBST(TreeNode, key):
    """
    二叉搜索树的插入操作，输入为树节点和关键字
    """
    result = SearchBST(TreeNode, key)
    if result[0]:
        print "Already in the tree!"
        return False
    if result[1].data < key:
        result.right = tree.BiTreeNode(key)
    elif result[1].data > key:      
        result.left = tree.BiTreeNode(key)
        
        
def DeleteBST(TreeNode, key):
    """
    二叉搜索树的删除操作，输入为树节点和关键字
    """
    target,parent = SearchBST(TreeNode, key)
    if target is None:
        print "Can't find the key!"
        return False
    targetPointer = findPointer(parent, target)
    if target.right is None:
        targetPointer.setValue(target.left)
    elif target.left is None:
        targetPointer.setValue(target.right)
    else:
        rightmost = target.left
        parent = target
        while rightmost:
            parent = rightmost
            rightmost = rightmost.right
        target.cargo = rightmost.cargo
        if target.left == rightmost:
            target.left = target.left.left
        else:
            parent.right = rightmost.left
        

class BalancedTreeNode(tree.BiTreeNode):
    def __init__(self, cargo, left=None, right=None, weight=None, bf=0):
        super(BalancedTreeNode, self).__init__(cargo, left, right, weight)
        self.balanceFactor = bf
        
    @staticmethod
    def rightRotate(BalancedTree, parent):
        willBeRoot = BalancedTree.left
        findPointer(parent, BalancedTree).setValue(willBeRoot)
        BalancedTree.left = willBeRoot.right
        willBeRoot.right = BalancedTree    

    @staticmethod
    def leftRotate(BalancedTree, parent):
        willBeRoot = BalancedTree.right
        findPointer(parent, BalancedTree).setValue(willBeRoot)
        BalancedTree.right = willBeRoot.left
        willBeRoot.left = BalancedTree
        
    @staticmethod
    def rigthBalance(BalancedTree, parent):
        rightChild = BalancedTree.right
        if rightChild.balanceFactor = 1:
            BalancedTreeNode.leftRotate()
        
    