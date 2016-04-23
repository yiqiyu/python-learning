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
        self.numVertexes = len(self.vexs)
        self.arc = [[INFINITY for col in range(self.numVertexes)] 
                   for row in range(self.numVertexes)]
        for i in range(self.numVertexes):
            self.arc[i][i] = 0
        if self.numVertexes:
            for edges in arcs:
                try:
                    self.arc[edges[0]][edges[1]] = edges[2]
                except IndexError:
                    #若元组第三个值不存在，则作为非网图处理
                    self.arc[edges[0]][edges[1]] = 1
                if not digraph:
                    #非有向图对称赋值
                    self.arc[edges[1]][edges[0]] = self.arc[edges[0]][edges[1]]
        self.numEdges = len(self.arc)
    
    @_Check
    def GetVex(self, u):
        return self.vexs[u]
    
    @_Check    
    def PutVex(self, v, value):
        self.vexs[v] = value
        
    @_Check  
    def FirstAdjvex(self, v):
        for i in range(self.numVertexes):
            if self.arcs[v][i] != INFINITY and self.arcs[v][i] != 0:
                return i
        
        
class EdgeNode(object):
    def __init__(self, adjvex, weight=1, nextedge=None):
        self.adjvex=adjvex
        self.weight=weight
        self.nextedge=nextedge
        
class VertexNode(object):
    def __init__(self, data, firstedge=None):
        self.data=data
        self.firstedge=firstedge
     
class GraphAdjList(MGraph):
    """
    邻接表描述的图
    """
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
            self.vexs[arc[0]].firstedge = t  
            try:
                t = EdgeNode(arc[0], arc[2])
            except IndexError:
                t = EdgeNode(arc[0])
            t.nextEdge = self.vexs(arc[1]).firstedge
            self.vexs[arc[1]].firstedge = t    

    def FirstAdjvex(self, v):
        return self.vexs[v].firstedge


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
                #将相同出节点的边连接起来，用头插法
                if arc2.visit == 1: continue
                if arc1.jvex == arc2.jvex and arc1 != arc2:
                    arc1.jlink = arc2.jlink
                    arc2.jlink = arc1
                    arc1.visit = 1
                    arc2.visit = 1 


class EdgeSetNode(object):
    def __init__(self, begin, end, weight=None):
        self.begin = begin
        self.end = end
        self.weight = weight
            
class EdgeSetArray(object):
    def __init__(self, vexs=[], arcs=[]):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        self.vexs = vexs
        try: 
            self.arcs = [EdgeSetNode(x[0], x[1], x[2]) for x in arcs]
        except IndexError:
            self.arcs = [EdgeSetNode(x[0], x[1], 1) for x in arcs]
            

def DFS(Graph):
    """
    图的深度优先遍历
    """
    visited = [False for i in range(Graph.numVertexes)]
    for i in range(Graph.numVertexes):
        if not visited[i]:
            if isinstance(Graph, MGraph):
                DFS_traverse_M(Graph, i, visited)
            elif isinstance(Graph, GraphAdjList):
                DFS_traverse(Graph, i, visited)

def DFS_traverse_M(Graph, i, visited):
    """
    深度优先遍历迭代部分，输入为邻接矩阵描述的图
    """
    visited[i] = True
    print Graph.vexs[i]
    for j in range(Graph.numVertexes):
        if not visited[j] and Graph.arcs[i][j] != INFINITY:
            DFS_traverse(Graph, j, visited)

def DFS_traverse(Graph, i, visited): 
    """
    深度优先遍历迭代部分，输入为邻接表描述的图
    """      
    visited[i] = True
    print Graph.vexs[i].data
    p = Graph.vexs[i].firstedge
    while p:
        if not visited[p.adjvex]:
            DFS_traverse(Graph, p.adjvex)
        p = p.nextedge


import stack

def BFS_L(Graph):
    """
    广度优先遍历迭代部分，输入为邻接表描述的图
    """  
    queue = stack.SqQueue(Graph.numVextexs)
    visited = [False for i in range(Graph.numVertexes)]
    for i in range(Graph.numVextexs):
        if not visited[i]:
            #头顶点入队
            visited[i] = True
            print Graph.vexs[i].data
            queue.EnQueue(Graph.vexs[i])
        while not queue.QueueEmpty():
            #出队
            p = queue.DeQueue().firstedge
            while p:
                if not visited[p.adjvex]:
                    #相邻顶点入队
                    visited[p.adjvex] = True
                    print Graph.vexs[p.adjvex].data
                    queue.EnQueue((Graph.vexs[p.adjvex],p.adjvex))
                p = p.nextedge
                
def BFS_M(Graph):
    """
    广度优先遍历迭代部分，输入为邻接表描述的图
    """  
    queue = stack.SqQueue(Graph.numVextexs)
    visited = [False for i in range(Graph.numVertexes)]
    for i in range(Graph.numVextexs):
        if not visited[i]:
            #头顶点入队
            visited[i] = True
            print Graph.vexs[i].data
            queue.EnQueue(i)
        while not queue.QueueEmpty():
            #出队
            p = queue.DeQueue()
            for j in range(Graph.numVextexs):
                if Graph.arcs[p][j] != INFINITY and (not visited[j]):
                    #相邻顶点入队
                    visited[j] = True
                    print Graph.vexs[j].data
                    queue.EnQueue(j)

