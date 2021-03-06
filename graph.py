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

def _CheckIndex(func):
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
    def __init__(self, vexs=None, arcs=None, digraph=0):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        参数digraph为零时，表示图为无向图，为1时则为有向图
        """
        if vexs is None: vexs = []
        if arcs is None: arcs = []
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
    
    @_CheckIndex
    def GetVex(self, u):
        return self.vexs[u]
    
    @_CheckIndex    
    def PutVex(self, v, value):
        self.vexs[v] = value
        
    @_CheckIndex  
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
    def __init__(self, vexs=None, arcs=None):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        if vexs is None: vexs = []
        if arcs is None: arcs = []
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
    """
    十字链表
    """
    def __init__(self, vexs=None, arcs=None):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        if vexs is None: vexs = []
        if arcs is None: arcs = []
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
    """
    多重邻接表
    """
    def __init__(self, vexs=None, arcs=None):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        if vexs is None: vexs = []
        if arcs is None: arcs = []
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
        
    def __str__(self):
        return "(%d, %d, weight:%d)" % (self.begin, self.end, self.weight)
            
class EdgeSetArray(object):
    """
    边集数组
    """
    def __init__(self, vexs=None, arcs=None):
        """
        图初始化，vexs输入一个一位数组，arcs为元组数组，每个元组代表
        由边的下标编号组成如（1,2），表示由v1与v2组成的边
        或（1,2,3），表示由v1与v2组成的边，权值为3
        """
        if vexs is None: vexs = []
        if arcs is None: arcs = []
        self.vexs = vexs
        try: 
            self.arcs = [EdgeSetNode(x[0], x[1], x[2]) for x in arcs]
        except IndexError:
            self.arcs = [EdgeSetNode(x[0], x[1], 1) for x in arcs]
        self.numVertexes = len(self.vexs)
            
    def MConvert(self, Graph):
        """
        矩阵描述的图转化成边集数组并按权值从小到大排序
        """
        self.vexs = Graph.vexs
        for i in range(Graph.numVertexes):
            for j in range(Graph.numVertexes):
                if Graph.arcs[i][j] and Graph.arcs[i][j] != INFINITY:
                    self.arcs.append(EdgeSetNode(i,j,Graph.arcs[i][j]))
        self.arcs.sort(key= lambda x: x.weight)
            

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
    queue = stack.SqQueue(Graph.numVertexes)
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
    顶点数据逐个打印
    """  
    queue = stack.SqQueue(Graph.numVextexs)
    visited = [False for i in range(Graph.numVertexes)]
    for i in range(Graph.numVertexes):
        if not visited[i]:
            #头顶点入队
            visited[i] = True
            print Graph.vexs[i].data
            queue.EnQueue(i)
        while not queue.QueueEmpty():
            #出队
            p = queue.DeQueue()
            for j in range(Graph.numVertexes):
                if Graph.arcs[p][j] != INFINITY and (not visited[j]):
                    #相邻顶点入队
                    visited[j] = True
                    print Graph.vexs[j].data
                    queue.EnQueue(j)
                    
def MST_Prim(Graph):
    """
    Prim算法实现的最小生成树函数，输入为邻接矩阵描述的图，权值为正
    输出为边集合
    """
#    AdjVex的值为树的边缘结点，下标与值表示两个顶点相连为权最小路径
    AdjVex = [0 for i in range(Graph.numVertexes)]
    LowCost = [i for i in Graph.arcs[0]]
    low = INFINITY
    for j in range(Graph.numVertexes):
        for i in range(Graph.numVertexes):
            if LowCost[i] and LowCost[i]<low:
                low = LowCost[i]
                NewVex = i
        print (AdjVex[NewVex], NewVex)
        LowCost[NewVex] = 0
        for i in range(Graph.numVertexes):
            if Graph.arcs[NewVex][i] < LowCost[i]:
                LowCost[i] = Graph.arcs[NewVex]
                AdjVex[i] = NewVex
 
def MST_Kruskal(Graph):
    """
    Kruskal算法实现的最小生成树函数，输入为邻接矩阵描述的图，权值为正
    输出为边集合
    """
    G = EdgeSetArray()
    G.MConvert(Graph)
    parent = [0 for i in G.numVertexes]
    for i in range(G.numVertexes):
        n = Find(parent, G.arcs[i].begin)
        m = Find(parent, G.arcs[i].end)
        if n != m:
            print G.arcs[i]
            parent[n] = m
            
def Find(parent, num):
    """
    回溯生成树的根节点
    输入parent表和节点下标，返回节点的根节点值
    """
    while parent[num] > 0:
        num = parent[num]
    return num

class SP_Dijkstra(object):
    """
    Dijkstra算法实现的最短路径生成函数
    """
    def __init__(self, Graph, vex0):
        self.begin = vex0
        self.visited = self.PathM = [0 for i in Graph.numVertexes]
        self.lowcost = [i for i in Graph.arcs[vex0]]
        self.visited[vex0] = 1
        for i in range(Graph.numVertexes):
            low = INFINITY
            for j in range(Graph.numVertexes):
                if not self.visited[j] and self.lowcost[j] < low:
                    NewVex = j
                    low = self.lowcost[j]
                self.visited[NewVex] = 1
            for j in range(Graph.numVertexes):
                if not self.visited[j] and (low+
                Graph.arcs[NewVex][j] < self.lowcost[j]):
                    self.lowcost[j] = low+Graph.arcs[NewVex][j]
                    self.PathM[j] = NewVex
                    
    def output(self, end):
        line = []
        t = end
        while t != self.begin:
            line.append((t, self.PathM[t]))
            t = self.PathM[t]
        for i in len(line):
            print line.pop()
            

class SP_Floyd(object):
    """
    Floyd算法实现的最短路径生成函数
    """
    def __init__(self, Graph):
        self.l = Graph.numVertexes
        self.PathM = [[i for i in range(Graph.numVertexes)] 
                        for i in range(Graph.numVertexes)]
        self.lowcost = [i for i in Graph.arcs]
        for i in range(Graph.numVertexes):
            for j in range(Graph.numVertexes):
                for k in range(Graph.numVertexes):
                    if self.lowcost[j][k] > (self.lowcost[j][i]+
                                             self.lowcost[i][k]):
                        self.lowcost[j][k] = (self.lowcost[j][i]+
                                              self.lowcost[i][k])
                        self.PathM[j][k] = self.PathM[k][i]
                        
    def PrintPath(self, begin, end):
        t =  self.PathM[begin][end]
        print '%d - %d path: %d' % (begin, end, t)
        while t != end:
            t = self.PathM[t][end]
            print "->"+t
        print "weight: "+self.lowcost[begin][end]
        

class TopologicalSort(object):
    """
    拓扑排序算法实现
    """
    Stack2 = []
    def __init__(self, LGraph, etv=None):
        etv = [] if etv is None else etv
        import copy
        Graph = copy.deepcopy(LGraph)
        count = 0
        #为图的顶点数组数据加上入度
        for vex in Graph.vexs:
            vex.ind = 0
        for vex in Graph.vexs:
            t = vex.firstedge
            Graph.vexs[t.adjvex].ind += 1
            while t.nextedge:
                Graph.vexs[t.adjvex].ind += 1
                t = t.nextedge
        Stack = []
        #一开始，入度为零的入栈
        for i in Graph.numVertexes:
            if Graph.vexs[i].ind == 0:
                Stack.append[(Graph.vexs[i], i)]
        while Stack:
            t = Stack.pop()
            self.Stack2.append(t[1])
            count += 1
            tt = t[0].firstedge
            pre = t[1]
            while tt:
                #去掉该顶点上的出边
                Graph.vexs[tt.adjvex].ind -= 1
                #同时判断是否有顶点入度为零，为零则入栈
                if not Graph.vexs[tt.adjvex].ind:
                    Stack.append[tt.adjvex]
                if etv:
                    #同一弧头中权最大的弧决定了事件最早开始时间
                    if etv[pre]+tt.weigth > etv[tt.adjvex]:
                        etv[tt.adjvex] = etv[pre]+tt.weigth            
                tt = tt.next
        if count < Graph.numVertexes:
            return "Error!"
        else:
            return "OK!"
        
    def output(self):
        if self.Stack2:
            for i in len(self.Stack2):
                print ("%d ->" % self.Stack2[i]),
        else:
            print "Error!"
            

def CriticalPath(Graph):
    """
    关键路径的算法实现
    """
    etv = [0 for i in range(Graph.numVertexes)]
    r = TopologicalSort(Graph, etv)
    ltv = [etv[Graph.numVertexes-1] for i in range(Graph.numVertexes)]
    while not r.Stack2:
        gettop = r.Stack2.pop()
        e = Graph.vexs[gettop].firstedge
        while e:
            k = e.adjvex
            if ltv[k]-e.weight < ltv[gettop]:
                ltv[gettop] = ltv[k]-e.weight
    for i in range(Graph.numVertexes):
        e = Graph.vexs[i].firstedge
        while e:
            k = e.adjvex
            ete = etv[i]
            lte = ltv[k]-e.weight
            if ete == lte:
                print "<v%d, v%d> length: %d" % (Graph.vexs[i].data, Graph.vexs[k].data,
                                                 e.weight)
                
        
        