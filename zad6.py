from zad3 import Graph, QueueBaE
from graphviz import Digraph


class Missionary:
    def __init__(self):
        self.y = {}
        n = 0
        for i in range(4):
            for j in range(4):
                for k in range(2):
                    self.y[n] = [i, j, k, 3 - i, 3 - j]
                    n += 1
        self.y_values = list(self.y.values())
        self.graph = Graph()
        self.graph.addVertex(30)

    def move_boat(self, situation):
        id = situation.id
        situation = self.y[id]
        boat = situation[2]
        if boat == 1:
            people = [situation[3], situation[4]]
        else:
            people = [situation[0], situation[1]]
        situations = [[1, 1], [2, 0], [0, 2], [1, 0], [0, 1]]
        for i in situations:
            x = [people[0] - i[0], people[1] - i[1]]
            good = True
            if x[0] < 0 or x[1] < 0:
                good = False
            elif x[1] > x[0] > 0:
                good = False
            elif 3 - x[1] > 3 - x[0] > 0:
                good = False
            if boat == 0 and good:
                key = self.y_values.index([x[0], x[1], 1, 3 - x[0], 3 - x[1]])
                if not self.graph.getVertex(key):
                    self.graph.addEdge(id, key)
                else:
                    self.graph.getVertex(key).setColor('gray')
            elif boat == 1 and good:
                key = self.y_values.index([3 - x[0], 3 - x[1], 0, x[0], x[1]])
                if not self.graph.getVertex(key):
                    self.graph.addEdge(id, key)
                else:
                    self.graph.getVertex(key).setColor('gray')

    def getEdges1(self):
        listOfEdges = []
        for i in self.graph.vertList.values():
            for j in i.connectedTo.keys():
                listOfEdges.append([i.id, j.id])
        return listOfEdges

    def createDot1(self):
        x = self.getEdges1()
        dot = Digraph()
        for i in x:
            text1 = str(self.y[i[0]])
            text2 = str(self.y[i[1]])
            dot.edge(text1, text2)
        dot.render('solution.gv', view=True)

    def creating_solution(self):
        start = self.graph.getVertex(30)
        vertQueue = QueueBaE()
        vertQueue.enqueue(start)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            if currentVert.id != 1:
                self.move_boat(currentVert)
            for nbr in currentVert.getConnections():
                if nbr.getColor() == 'gray':
                    pass
                else:
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')
        self.createDot1()
