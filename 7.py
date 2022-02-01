from zad3 import Graph
from pythonds.graphs import PriorityQueue

def dijkstra(aGraph, start, goal):
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

    for i in [aGraph.getVertex((goal, 0))]:
        paths = []
        while i != start:
            paths.append(i.id)
            if i.getPred:
                i = i.getPred()

        paths.append(start.id)
        paths.reverse()
        print(paths)

def canisters(can1 = 4, can2 = 3, goal = 2):
    if can1 < goal and can2 < goal:
        raise ValueError("Can't reach the goal.")
    if can1 <= can2 :
        raise ValueError("Canister1 must be bigger than canister2")
    if can1 == goal or can2 == goal:
        raise ValueError("You've already reach the goal.")
    if not (type(can1) == int and type(can2) == int and type(goal) == int):
        raise ValueError("Capacity of canisters and the goal must be integers.")

    graph = Graph()
    for i in range(can1 + 1):
        for j in range(can2 + 1):
            graph.addVertex((i, j))
    for v in list(graph.vertList.keys()):
        graph.addEdge(v, (can1, v[1]))
        graph.addEdge(v, (v[0], can2))

        if v[0] + v[1] <= can2:
            graph.addEdge(v, (0, v[0] + v[1]))
        else:
            graph.addEdge(v, (v[0] - can2 + v[1], can2))

        if v[0] + v[1] <= can1:
            graph.addEdge(v, (v[0] + v[1], 0))
        else:
            graph.addEdge(v, (can1, v[1] - can1 + v[0]))

        graph.addEdge(v, (0, v[1]))
        graph.addEdge(v, (v[0], 0))

    dijkstra(graph, graph.getVertex((0,0)), goal)




print(canisters(6,4,5))


