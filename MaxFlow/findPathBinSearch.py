import GraphReader.dimacs as dimacs


class Graph:
    def __init__(self, E, V):
        self.V = V
        self.adj = []
        for i in range(V+1):
            self.adj.append([0]*(V+1))
        for edge in E:
            self.adj[edge[0]][edge[1]] = edge[2]
            self.adj[edge[1]][edge[0]] = edge[2]

def BFS(G, s, t, flow):
    visited = [False]*G.V
    parent = [-1]*G.V
    q = []
    q.append(s)
    visited[s] =True
    
    while len(q) != 0:
        v = q.pop(0)
        for i in range(G.V):
            if not visited[i] and G.adj[v][i] >= flow:
                q.append(i)
                visited[i] = True
                parent[i] = v

    if visited[t]:
        path = []
        v = t
        while v != -1:
            path.insert(0, v)
            v = parent[v]
        return (flow, path)
    else: 
        return (0, [])

def findBestPath(G, s, t):
    graph = Graph(G[1], G[0])
    edges = G[1]
    edges = sorted(edges, key=lambda edge: edge[2])
    q = len(edges)-1
    p = 0
    if len(BFS(graph, s, t, edges[q][2])[1]) > 0:
        return edges[q][2]
    if len(BFS(graph, s, t, edges[p][2])[1]) == 0:
        return 0
    while p < q-1:
        half = int((p+q)/2)
        flow = BFS(graph, s, t, edges[half][2])[0]
        if flow > 0:
            p = half
        elif flow == 0:
            q = half

    if len(BFS(graph, s, t, edges[q][2])[1]) > 0:
        return edges[q][2]
    else:
        return edges[p][2]




# print("Expected: 4")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/g1"), 1, 2), '\n')

# print("Expected: 90")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique5"), 1, 2), '\n')

# print("Expected: 89")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique20"), 1, 2), '\n')

# print("Expected: 98")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique100"), 1, 2), '\n')

# print("Expected: 99")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique1000"), 1, 2), '\n')

# print("Expected: 9")
# print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/grid5x5"), 1, 2), '\n')

print("Expected: 2735")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/grid100x100"), 1, 2), '\n')

print("Expected: 11")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/path10"), 1, 2), '\n')

print("Expected: 10")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/path1000"), 1, 2), '\n')

print("Expected: 10")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/path10000"), 1, 2), '\n')

print("Expected: 4")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/pp10"), 1, 2), '\n')

print("Expected: 64")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/pp100"), 1, 2), '\n')

print("Expected: 960")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/pp1000"), 1, 2), '\n')

print("Expected: 68")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/rand20_100"), 1, 2), '\n')

print("Expected: 344")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/rand100_500"), 1, 2), '\n')

print("Expected: 99301")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/rand1000_100000"), 1, 2), '\n')

