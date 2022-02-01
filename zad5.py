from pythonds.graphs import PriorityQueue
from zad3 import Graph

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)

    for i in aGraph:
        print("Shortest path from " + str(start.id) + " to " + str(i.id) + ", distance: " + str(i.dist))
        paths = []

        while i != start:
            paths.append(i.id)
            i = i.getPred()

        paths.append(start.id)
        paths.reverse()
        print(paths)
