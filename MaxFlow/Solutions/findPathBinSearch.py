import sys
sys.path.append('/home/andrzej/GraphsLab/MaxFlow/GraphReader')
import dimacs


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
    visited = [False]*(G.V+1)
    parent = [-1]*(G.V+1)
    q = []
    q.append(s)
    visited[s] =True
    
    while len(q) != 0:
        v = q.pop(0)
        for i in range(1,G.V+1):
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
    if BFS(graph, s, t, edges[q][2])[0] > 0:
        return edges[q][2]
    if BFS(graph, s, t, edges[p][2])[0] == 0:
        return 0
    while p < q-1:
        half = int((p+q)/2)
        flow = BFS(graph, s, t, edges[half][2])[0]
        if flow > 0:
            p = half
        elif flow == 0:
            q = half

    if BFS(graph, s, t, edges[q][2])[0] > 0:
        return edges[q][2]
    else:
        return edges[p][2]


print(findBestPath(dimacs.loadWeightedGraph(sys.argv[1]),1,2))


