# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 18:56:40 2016

@author: Dante Yu

图的定义以及常用方法，另外还有遍历算法、两种最小生成树算法最短路径算法的实现
"""

INFINITY = 999999


class GraphException(Exception):
    pass


import functools

def _Check(func):
    """
    类方法的装饰器，判断输入的下标是否超出。
    否则将抛出异常
    """
    @functools.wraps(func)
    def wrapper(self, v):
        try:
            return func(self, v)
        except IndexError:
            raise GraphException("Can't find the vertex")
    return wrapper

    
class MGraph(object):
    """
    邻接矩阵描述的图
    """
    def __init__(self, vexs=[], arcs=[], digraph=0):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        参数digraph为零时，表示图为无向图，为1时则为有向图
        """
        self.vexs = vexs
        numVertexes = len(self.vexs)
        self.arc = [[INFINITY for col in range(numVertexes)] 
                   for row in range(numVertexes)]
        if numVertexes:
            for edges in arcs:
                try:
                    self.arc[edges[0]][edges[1]] = edge[2]
                except IndexError:
                    #若元组第三个值不存在，则作为非网图处理
                    self.arc[edges[0]][edges[1]] = 1
                if not digraph:
                    #非有向图对称赋值
                    self.arc[edges[1]][edges[0]] = self.arc[edges[0]][edges[1]]
        numEdges = len(self.arc)
    
    @_Check
    def GetVex(self, u):
        return self.vexs[u]
    
    @_Check    
    def PutVex(self, v, value):
        self.vexs[v] = value


class EdgeNode(object):
    def __init__(self, adjvex, weight=1, nextEdge=None):
        self.adjvex=adjvex
        self.weight=weight
        self.nextEdge=nextEdge
        
class VertexNode(object):
    def __init__(self, data, firstedge=None):
        self.data=data
        self.firstedge=firstedge
     
class GraphAdjList(object):
    def __init__(self, vexs=[], arcs=[]):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        self.vexs = [VertexNode(x) for x in vexs]
        self.numVertexes = len(self.vexs)
        self.numEdges = len(arcs)
        for arc in arcs:
            try:
                t = EdgeNode(arc[1], arc[2])
            except IndexError:
                #若元组第三个值不存在，则作为非网图处理，下同
                t = EdgeNode(arc[1])
            t.nextEdge = self.vexs(arc[0]).firstedge
            self.vexs(arc[0]).firstedge = t  
            try:
                t = EdgeNode(arc[0], arc[2])
            except IndexError:
                t = EdgeNode(arc[0])
            t.nextEdge = self.vexs(arc[1]).firstedge
            self.vexs(arc[1]).firstedge = t     


class OEdgeNode(object):
    def __init__(self, tailvex, headvex, weight=1, headlink=None, 
                 taillink=None):
        self.tailvex = tailvex
        self.headvex = headvex
        self.weight = weight
        self.headlink = headlink
        self.taillink = taillink
        
class OVertexNode(object):
    def __init__(self, data, firstin=None, firstout=None):
        self.data = data
        self.firstin = firstin
        self.firstout = firstout

class OrthogonalList(object):
    def __init__(self, vexs=[], arcs=[]):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        self.vexs = [OVertexNode(x) for x in vexs]
        self.numVertexes = len(self.vexs)
        self.numEdges = len(arcs)
        for arc in arcs:
            try:
                t = OEdgeNode(arc[0], arc[1], arc[2])
            except IndexError:
                #若元组第三个值不存在，则作为非网图处理，下同
                t = OEdgeNode(arc[0], arc[1])
            t.taillink = self.vexs(arc[1]).firstin
            self.vexs(arc[1]).firstin = t  
            t.headlink = self.vexs(arc[0]).firstout
            self.vexs(arc[0]).firstout = t 
            

class MEdgeNode(object):
    def __init__(self, ivex, jvex, weight=1, ilink=None, 
                 jlink=None):
        self.ivex = ivex
        self.jvex = jvex
        self.weight = weight
        self.ilink = ilink
        self.jlink = jlink
        self.visit = 0

class GraphAdjListMulti(object):
    def __init__(self, vexs=[], arcs=[]):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        self.vexs = [VertexNode(x) for x in vexs]
        self.numVertexes = len(self.vexs)
        self.numEdges = len(arcs)
        _match1 = [None]* self.numEdges
        _match2 = [None]* self.numEdges
        _match = []
        for arc in arcs:
            try:
                t = MEdgeNode(arc[0], arc[1], arc[2])
            except IndexError:
                #若元组第三个值不存在，则作为非网图处理，下同
                t = MEdgeNode(arc[0], arc[1])
            t.ilink = self.vexs(arc[0]).firstedge
            self.vexs(arc[0]).firstedge = t
            _match.append(t)
        for arc1 in _match:
            for arc2 in _match:
                if arc2.visit == 1: continue
                if arc1.jvex == arc2.jvex and arc1 != arc2:
                    arc1.jlink = arc2.jlink
                    arc2.jlink = arc1
                    arc1.visit = 1
                    arc2.visit = 1 
            

                

