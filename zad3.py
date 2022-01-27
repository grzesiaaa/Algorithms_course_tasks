import sys
import graphviz


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'  # new: color of node
        self.dist = sys.maxsize  # new: distance from beginning (will be used later)
        self.pred = None  # new: predecessor
        self.disc = 0  # new: discovery time
        self.fin = 0  # new: end-of-processing time

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def getId(self):
        return self.id


class QueueBaE(object):
    def __init__(self):
        self.list_of_items = []

    def enqueue(self, item):
        self.list_of_items.insert(0, item)

    def dequeue(self):
        return self.list_of_items.pop()

    def is_empty(self):
        return self.list_of_items == []

    def size(self):
        return len(self.list_of_items)

    def __str__(self):
        return str(self.list_of_items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def getEdges(self, p=0):
        listOfEdges = []
        if p != 0:
            for i in self.vertList.values():
                x = []
                for j in i.connectedTo.keys():
                    x.append((i.id, j.id))
                listOfEdges.append(x)
            while [] in listOfEdges:
                listOfEdges.remove([])
            listOfEdges.sort(key=lambda x: len(x), reverse=True)
            for i in listOfEdges:
                print(*i)
        else:
            for i in self.vertList.values():
                for j in i.connectedTo.keys():
                    listOfEdges.append((i.id, j.id))
        return listOfEdges

    def createDot(self):
        x = self.getEdges()
        dot = graphviz.Digraph()
        for i in x:
            text_1 = str(i[0]) + '\n dist ' + str(i[1])
            text_2 = str(i[2]) + '\n dist ' + str(i[3])
            dot.edge(text_1, text_2, label=str(i[4]))
        dot.render('solution.gv', view=True)

    def __len__(self):
        return len(self.getVertices())

    def __iter__(self):
        return iter(self.vertList.values())

    def show(self):
        for v in self:
            for w in v.getConnections():
                print("( %s , %s )" % (v.getId(), w.getId()))

    def bfs(self, start):
        start.setDistance(0)
        start.setPred(None)
        vertQueue = QueueBaE()
        vertQueue.enqueue(start)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')

    def traverse(self, start):
        x = start
        while x.getPred():
            print(x.getId())
            x = x.getPred()
        print(x.getId())

    def dfs(self):
        for aVertex in self.vertList.values():
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self.vertList.values():
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


