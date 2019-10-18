from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue) != 0:
            v = queue.pop(0)
            for idx, val in enumerate(self.graph[v]):
                if visited[idx] == False and val > 0:
                    visited[idx] = True
                    queue.append(idx)
                    parent[idx] = v
                
        return visited[t]

    def FordFulkerson(self, source, sink):
        parents = [-1]*(self.ROW)
        max_flow = 0
        while(self.BFS(source, sink, parents)):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parents[s]][s])
                s = parents[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parents[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u 

        return max_flow


graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 
  
g = Graph(graph) 
  
source = 0; sink = 5
   
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))



        