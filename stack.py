# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:33:49 2016

@author: Yiqi Yu

栈及其方法的实现，包括顺序栈和链栈，队列
"""
from list import Node

class StackException(Exception):
    pass

class SqStack:
    def __init__(self, Max):
        self.data=[]
        self.max=Max
        self.top=len(self.data)
        
    def Push(self, data):
        if self.top<=self.max:
            self.data.append(data)
            self.top+=1
        else:
            raise StackException("Stack is full")
            
    def Pop(self):
        if self.top>0:
            self.data.pop()
            self.top=self.top-1
        else:
            raise StackException("Stack is empty")
            
class LinkedStack:
    def __init__(self):
        self.length=0
        self.top=self
    
    def Push(self, node):
        node.next=self.top
        self.top=node
        self.length+=1
        
    def Pop(self):
        if self.length==0:
            raise StackException("Stack is empty")
        result=self.top.cargo
        self.top=self.top.next
        self.length-=1
        return result

class QueueException(Exception):
    pass

class SqQueue:
    def __init__(self, Max):
        self.data=[]
        self.max=Max
        self.front=0
        self.rear=0
        self.length=0
        
    def QueueLength(self):
        return (self.rear-self.front+self.max)%self.max
        
    def EnQueue(self, item):
        if self.QueueLength()==self.max:
            raise QueueException("Stack is full")
        self.data[self.rear]=item
        self.rear=(self.rear+1)%self.max

    def DeQueue(self):
        if self.front==self.rear:
            raise QueueException("Stack is empty")
        result=self.data[self.front]
        self.front=(self.front+1)%self.max
        return result
     
class LinkedQueue:
    def __init__(self):
        self.length=0
        self.front=self
        self.rear=self
        
    def EnQueue(self, node):
        self.rear.next=node
        self.rear=node
        self.length+=1
        
    def DeQueue(self):
        if self.length==0:
            raise StackException("Stack is empty")
        result=self.front.cargo
        self.front=self.front.next
        return result
        