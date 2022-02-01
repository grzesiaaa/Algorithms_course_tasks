from zad3 import Graph
from zad5 import shortest_way

def canisters(can1 = 4, can2 = 3, goal = 2):
    if can1 < goal and can2 < goal:
        raise ValueError("Can't reach the goal.")
    if can1 == can2:
        raise ValueError("Canisters can't be the same size.")
    if can1 == goal or can2 == goal:
        raise ValueError("You've already reach the goal.")
    if not (type(can1) == int and type(can2) == int and type(goal) == int):
        raise ValueError("Capacity of canisters and the goal must be integers.")

    graph = Graph()
    for i in range(can1 + 1):
        for j in range(can2 + 1):
            graph.addVertex((i, j))
    for v in list(graph.vertList.keys()):
        # napelniamy 1 lub 2 do pelna
        graph.addEdge(v, (can1, v[1]))
        graph.addEdge(v, (v[0], can2))

        if v[0] + v[1] <= can2:
            graph.addEdge(v, (0, v[0] + v[1])) #calosc z 1 do 2
        else:
            graph.addEdge(v, (v[0] - can2 + v[1], can2)) # dopelniamy 2 do pelna z 1

        if v[0] + v[1] <= can1:
            graph.addEdge(v, (v[0] + v[1], 0)) # calosc z 2 do 1
        else:
            graph.addEdge(v, (can1, v[1] - can1 + v[0])) # dopelniamy 1 do pelna z 2

        graph.addEdge(v, (0, v[1]))
        graph.addEdge(v, (v[0], 0))

    graph.show()


print(canisters())



