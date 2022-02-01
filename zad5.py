from pythonds.graphs import PriorityQueue


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

    p = []
    print("Shortest paths from " + str(start.id))
    for i in aGraph:
        paths = []
        while i is not start:
            paths.append(i.id)
            i = i.getPred()
        paths.append(start.id)
        paths.reverse()
        p.append(paths)
    dict = {}
    for key in list(g.getVertices()):
        dict[key] = len(p[key])-1
    return dict
