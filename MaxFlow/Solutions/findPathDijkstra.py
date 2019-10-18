import sys
sys.path.append('/home/andrzej/GraphsLab/MaxFlow/GraphReader')
import dimacs
import math
import heapq


def findBestPath(G, s, t):
    E = G[1]
    adj = []
    for i in range(0, G[0]+1):
        adj.append([0]*(G[0]+1))
    for edge in E:
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]

    V = [-1]*(G[0]+1)
    V[s] = math.inf
    Q = []
    Q.append(((-1)*V[s],s))
    heapq.heapify(Q)


    while len(Q) != 0:
        v = heapq.heappop(Q)
        v = (-1*v[0],v[1])
        for u in range(1, G[0]+1):
            if adj[v[1]][u] > 0 and min(adj[v[1]][u],v[0]) > V[u]:
                V[u] = min(adj[v[1]][u],v[0])
                heapq.heappush(Q,((-1)*V[u], u))
    
    return V[t]


print(findBestPath(dimacs.loadWeightedGraph(sys.argv[1]),1,2))
 
    
