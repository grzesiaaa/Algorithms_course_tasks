import graphviz


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

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
            dot.edge(str(i[0]), str(i[1]))
        dot.render('solution.gv', view=True)

    def __len__(self):
        return len(self.getVertices())

    def __iter__(self):
        return iter(self.vertList.values())

    def show(self):
        for v in self:
            for w in v.getConnections():
                print("( %s , %s )" % (v.getId(), w.getId()))
