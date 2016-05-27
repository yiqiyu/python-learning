# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:37:00 2016

@author: Administrator
"""

import tree

def SearchBST(TreeNode, key, parent=None):
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
    result = SearchBST(TreeNode, key)[0].cargo
    if result < key:
        result.right = tree.BiTreeNode(key)
    elif result > key:
        result.left = tree.BiTreeNode(key)
    else:
        print "Already in the tree!"

        
def DeleteBST(TreeNode, key):
    try:    
        target,parent = SearchBST(TreeNode, key)
    except ValueError:
        print "Can't find the key!"
        return None
    enum = {}
    flag = "right" if parent.right == target else "left"
    if target.right is None:
        if  parent.right == target:  
            parent.right = target.left
        elif parent.left == target:
            parent.left == target.left
    elif target.left is None:
        
        