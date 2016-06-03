# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:37:00 2016

@author: Administrator
"""

import tree

def SearchBST(TreeNode, key, parent=None):
    """
    二叉搜索树的查找操作，输入为树节点和关键字
    """
    if not TreeNode:
        print False
        return parent
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
    result = SearchBST(TreeNode, key)[0].cargo
    if result < key:
        result.right = tree.BiTreeNode(key)
    elif result > key:
        result.left = tree.BiTreeNode(key)
    else:
        print "Already in the tree!"

        
def DeleteBST(TreeNode, key):
    """
    二叉搜索树的删除操作，输入为树节点和关键字
    """
    try:    
        target,parent = SearchBST(TreeNode, key)
    except ValueError:
        print "Can't find the key!"
        return None
    parentSideThatTargetTook = {"right": parent.right, "left": parent.left}
    side = "right" if parent.right == target else "left"
    if target.right is None:
        parentSideThatTargetTook[side] = target.left
    elif target.left is None:
        parentSideThatTargetTook[side] = target.right
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
        
        