def topology_dfsvisit(g, tp, startVertex):
    topology_sort = tp
    startVertex.setColor('gray')
    g.time += 1
    startVertex.setDiscovery(g.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            topology_dfsvisit(g, topology_sort, nextVertex)
    startVertex.setColor('black')
    g.time += 1
    startVertex.setFinish(g.time)
    topology_sort.append(startVertex)
    return topology_sort


def topology_dfs(g):
    topology_sort = []
    g.time = 0
    for aVertex in g.vertList.values():
        aVertex.setColor('white')
        aVertex.setPred(-1)
        aVertex.setDiscovery(0)
        aVertex.setFinish(0)
    for aVertex in g.vertList.values():
        if aVertex.getColor() == 'white':
            topology_sort = topology_dfsvisit(g, topology_sort, aVertex)
    text = ''
    topology_sort.reverse()
    for i in topology_sort:
        text += "Id: " + str(i.id) + ' Disc/Fin: ' + str(i.disc) + '/' + str(i.fin) + "\n"
    print(text)
