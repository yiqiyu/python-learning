# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:21:21 2016

@author: Administrator
"""

class TreeException(Exception):
    pass

class BiTreeNode:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)
        
class BiTree(BiTreeNode):
    pass

import functools

def TypeCheck(ctype1, ctype2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(node):
            if not (isinstance(node, ctype1) or isinstance(node, ctype2)):
                raise TreeException("Input Error")
            return func(node)
        return wrapper
    return decorator
  
@TypeCheck(BiTreeNode, BiTree)
def PreOrderTraverse(node):
    if node==None:
        return
    print node.cargo
    PreOrderTraverse(node.left)
    PreOrderTraverse(node.right)

@TypeCheck(BiTreeNode, BiTree)
def InOrderTraverse(node):
    if node==None:
        return
    PreOrderTraverse(node.left)
    print node.cargo
    PreOrderTraverse(node.right)

@TypeCheck(BiTreeNode, BiTree)
def PostOrderTraverse(node):
    if node==None:
        return
    PreOrderTraverse(node.left)
    PreOrderTraverse(node.right)
    print node.cargo
    
@TypeCheck(BiTreeNode, BiTree)
def CreateBiTree(node):
    ch=raw_input("input data:\t")
    if ch=='#':
        node=None
    else:
        node=BiTreeNode(ch)
        CreateBiTree(node.left)
        CreateBiTree(node.right)
        
class BiTreadTreeNode(BiTreeNode):
    def __init__(self, cargo, left=None, right=None):
        BiTreeNode.__init__(cargo, left=None, right=None)
        self.ltag='link'
        self.rtag='link'
        
class BiTreadTree(BiTreadTreeNode):
    pass

@TypeCheck(BiTreadTreeNode, BiTreadTree)        
def InTreading(node):
    pre=[node]
    _InTreading(node, pre)
    
def _InTreading(node, pre):
    precur=pre.pop()
    if node!=None:
        _InTreading(node.left, pre)
        if node.left==None:
            node.ltag="thread"
            node.left=precur
        if precur.right==None:
            precur.rtag="thread"
            precur.right=node
        pre.append(node)
        _InTreading(node.right, pre)

@TypeCheck(BiTreadTreeNode, BiTreadTree)                
def InOrderTraverse_Thr(node):
    T=node.left
    while T!=node:
        while T.ltag=='link':
            T=T.left
        print T.cargo
        while T.rtag=='thread' and T.right!=node:
            T=T.right
            print T.cargo
        T=T.right
        
def ForestToTree(*forest):
    t=forest[0]
    for tree in forest:
        if t==tree:
            continue
        t.right=tree
        t=tree

def HuffmanTreeCreate(nlist):
    nlist.sort(reverse=True)
    tweigh=None
    for i in range(len(nlist)):
        e=nlist.pop()
        if not tweigh:
            troot=BiTreeNode(e[0])
            tweigh=e[1]
            continue
        if e[0]<tweigh:
            nl=BiTreeNode(e[0])
            tweigh=tweigh+e[1]
            troot=BiTreeNode(tweigh,nl,troot)
        else:
            nr=BiTreeNode(e[0])
            tweigh=tweigh+e[1]
            troot=BiTreeNode(tweigh,troot,nr)
    return troot
    
        