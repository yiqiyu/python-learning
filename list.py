# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:33:14 2016

@author: Dante Yu

线性表的代码实现，包括顺序储存表，单链表和环形链表结构，及各自的方法
"""

#list的异常
class ListException(Exception):
    pass

#顺序储存表
class SqList:
    def __init__(self, max):
        self.max=max
        self.data=[]
        self.length=len(self.data)
     
     #按位置获得元素
    def GetItem(self, loc):
        if loc<1 or loc>self.length or (not type(loc)==int):
            raise ListException("Sqlist Error")
        return self.data[loc-1]
    
    #按位置之后插入元素
    def ListInsert(self, item, loc):
        if loc>self.max:
            raise ListException("List is Full")
        if loc<1 or loc>self.length or (not type(loc)==int):
            raise ListException("Sqlist Error")
        if not loc==self.length:
            i=self.length-1
            while i>loc-1:
                self.data[i+1]=self.data[i]
                i=i-1
        self.data[loc-1]=item
        self.length=self.length+1
        return
    
    #删除指定元素并返回值
    def ListDelete(self, loc):
        if self.length==0:
            raise ListException("List is empty")
        if loc<1 or loc>self.length or (not type(loc)==int):
            raise ListException("Sqlist Error")
        item=self.data[loc-1]
        if not loc==self.length:
            i=loc-1
            while i<self.length-1:
                self.data[i]=self.data[i+1]
                i=i+1
        self.length=self.length-1
        return item

#节点        
class Node:
    def __int__(self, cargo, Nnext):
        self.cargo=cargo
        self.next=Nnext

#链表        
class LinkedList:
    def __int__(self):
        self.length=0
        self.next=None
        
    def search(self, loc):
        i=1
        item=self.next
        while i<loc:
            item=self.next
            if not item:
                raise ListException("Can't locate item")
            i=i+1
        return item
        
    def Append(self, node):
        item=self.search(self.length)
        node.next=None
        item.next=node
        self.length=self.length+1
        
    def GetItem(self, loc):
        if loc<1 or loc>self.length or (not type(loc)==int):
            raise ListException("Input Error")
        return self.search(loc).cargo
        
    def ListInsert(self, loc, node):
        if loc<1 or (not type(loc)==int):
            raise ListException("Input Error")
        item=self.search(loc)
        node.next=item.next
        item.next=node
        self.length=self.length+1
        
    def ListDelete(self, loc):
        if loc<1 or (not type(loc)==int):
            raise ListException("Input Error")
        item=self.search(loc-1)
        deleted=item.next.cargo
        item.next=item.next.next  
        self.length=self.length-1
        return deleted

#环形链表
class CircularList(LinkedList):
    def __init__(self):
        self.length=0
        self.next=self
        
    #override LinkedList.Append
    def Append(self, node):
        item=self.search(self.length)
        node.next=self
        item.next=node
        self.length=self.length+1
 
#双向节点       
class DoubleNode(Node):
    def __int__(self, cargo, prior, Nnext):
        Node.__int__(self, cargo, Nnext)
        self.prior=prior
        
#双向链表
class DoubleList(CircularList):
    def __init__(self):
        LinkedList.__int__(self)
        self.prior=self
        
    def Append(self, node):
        LinkedList.Append(self, node)
        self.prior=node
        
    def ListInsert(self, loc, node):
        if loc<1 or (not type(loc)==int):
            raise ListException("Input Error")
        item=self.search(loc)
        node.next=item.next
        node.prior=item
        item.next.prior=node
        item.next=node
        self.length=self.length+1
    
    def ListDelete(self, loc):
        if loc<1 or (not type(loc)==int):
            raise ListException("Input Error")
        item=self.search(loc-1)
        deleted=item.next.cargo
        item.next.next.prior=item
        item.next=item.next.next  
        self.length=self.length-1
        return deleted