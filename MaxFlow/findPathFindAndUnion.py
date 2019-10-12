import GraphReader.dimacs as dimacs

class Vertex:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.ownedSetSize = 1

def find(vertex):
    while vertex.parent != vertex:
        vertex = vertex.parent
    return vertex

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1.ownedSetSize > v2.ownedSetSize:
        v2.parent = v1
        v1.ownedSetSize += v2.ownedSetSize
    else:
        v1.parent = v2
        v2.ownedSetSize += v1.ownedSetSize

def findBestPath(G, s, t):
    V = []
    for i in range(1, G[0]+1):
        V.append(Vertex(i))
    L = G[1]
    L = sorted(L, key=lambda edge: edge[2], reverse = True)
    for edge in L:
        union(V[edge[0]-1], V[edge[1]-1])
        if find(V[s-1]) == find(V[t-1]):
            return edge[2]
    
print("Expected: 4")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/g1"), 1, 2))

print("Expected: 90")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique5"), 1, 2))

print("Expected: 89")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique20"), 1, 2))

print("Expected: 98")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique100"), 1, 2))

print("Expected: 99")
print("Actual: ", findBestPath(dimacs.loadWeightedGraph("MaxFlow/SampleGraphs/clique1000"), 1, 2))


