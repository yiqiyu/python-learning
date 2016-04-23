# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:21:21 2016

@author: Dante Yu

文件包括了二叉树、线索二叉树和赫夫曼树的类定义以及方法的实现

"""

#树操作中的异常
class TreeException(Exception):
    pass


class BiTreeNode(object):
    """
    二叉树节点的定义
    """
    def __init__(self, cargo, left=None, right=None, weight=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        self.weight = weight
        
    def __str__(self):
        return str(self.cargo)
      

class BiTree(BiTreeNode):
    """
    二叉树根节点的定义
    """
    pass


import functools

def TypeCheck(ctype1, ctype2):
    """
    树操作函数的装饰器，负责检查输入的类型，ctype1和ctype2参数传入的是树的节点或树的根节点
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(node):
            #若类型不符合，则抛出树的异常
            if not (isinstance(node, ctype1) or isinstance(node, ctype2)):
                raise TreeException("Input Error")
            return func(node)
        return wrapper
    return decorator

@TypeCheck(BiTreeNode, BiTree)
def PreOrderTraverse(node):
    """
    普通二叉树的前序遍历
    """
    if node==None:
        return
    print node.cargo
    PreOrderTraverse(node.left)
    PreOrderTraverse(node.right)

@TypeCheck(BiTreeNode, BiTree)
def InOrderTraverse(node):
    """
    普通二叉树的中序遍历
    """
    if node==None:
        return
    PreOrderTraverse(node.left)
    print node.cargo
    PreOrderTraverse(node.right)

@TypeCheck(BiTreeNode, BiTree)
def PostOrderTraverse(node):
    """
    普通二叉树的后序遍历
    """
    if node==None:
        return
    PreOrderTraverse(node.left)
    PreOrderTraverse(node.right)
    print node.cargo


@TypeCheck(BiTreeNode, BiTree)
def CreateBiTree(node):
    """
    二叉树生成函数，前序遍历实现
    """
    #每次迭代就会要求输入一次节点的值
    ch=raw_input("input data:\t")
    #若输入为‘#’，意味着该节点为空
    if ch=='#':
        node=None
    else:
        node=BiTreeNode(ch)
        CreateBiTree(node.left)
        CreateBiTree(node.right)
 
       
class BiTreadTreeNode(BiTreeNode):
    """
    线索二叉树节点定义
    """
    def __init__(self, cargo, left=None, right=None):
        BiTreeNode.__init__(cargo, left=None, right=None)
        #比一般二叉树节点多出两个标签，‘link’表示孩子指向节点，‘thread’表示孩子指向前驱或后继
        self.ltag = 'link'
        self.rtag = 'link'
        
class BiTreadTree(BiTreadTreeNode):
    """
    线索二叉树根节点定义
    """
    pass

@TypeCheck(BiTreadTreeNode, BiTreadTree)        
def InTreading(node):
    """
    线索二叉树线索化
    """
    #前驱储存为pre
    pre = [node]
    #迭代操作另外定义
    _InTreading(node, pre)
   
def _InTreading(node, pre):
    """
    线索二叉树线索化迭代部分，中序遍历实现
    """
    precur = pre.pop()
    if node != None:
        _InTreading(node.left, pre)
        #叶子节点左孩子改为线索，指向前驱
        if node.left == None:
            node.ltag = "thread"
            node.left = precur
        #前驱的后继指向本叶子节点
        if precur.right == None:
            precur.rtag = "thread"
            precur.right = node
        #更新前驱位置为本节点
        pre.append(node)
        _InTreading(node.right, pre)

@TypeCheck(BiTreadTreeNode, BiTreadTree)                
def InOrderTraverse_Thr(node):
    """
    线索二叉树线索化后的中序遍历
    """
    T = node.left
    while T != node:
        while T.ltag == 'link':
            T = T.left
        print T.cargo
        #到了叶子节点，改为寻找后继
        while T.rtag == 'thread' and T.right != node:
            T = T.right
            print T.cargo
        #左孩子遍历完毕，改为右孩子
        T = T.right
 
      
def ForestToTree(*forest):
    """
    二叉树森林合成为一个二叉树。
    参数个数不限，参数为以孩子兄弟表示法表示的一般树。
    """
    t = forest[0]
    #新树会被加在上一棵树的右孩子
    for tree in forest:
        if t == tree:
            continue
        t.right = tree
        t = tree

import copy

def HuffmanTreeCreate(List):
    """
    赫夫曼标码实现函数。
    nlist为节点表，节点以元组表示，元组第一个元素为内容，第二个元素为权。
    返回一个树根节点
    """
    #按权降序排列节点
    nlist = copy.deepcopy(List)
    nlist.sort(key=lambda x:x[1], reverse=True)
    #创建树数组
    tlist = [BiTreeNode(n[0], weight=n[1]) for n in nlist]
    NewWeigh = None
    MaxTime = len(nlist)
    for i in range(MaxTime):
        e1 = tlist.pop()
        e2 = tlist.pop()
        NewWeigh = e2.weight+e1.weight
        NewRoot = BiTreeNode(NewWeigh,e1,e2)
        j = -1
        #将新树节点从末端插入正确位置
        while True:
            if tlist[j].weight > NewRoot.weight:
                tlist[(j+1):(j+1)] = [NewRoot]
                break
            j -= 1
    return tlist.pop()
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)