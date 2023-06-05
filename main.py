from collections import deque


class BFSTraversal:
    def __init__(self, v):
        self.node = v
        self.adj = [[] for _ in range(v)]

    def insertEdge(self, v, w):
        self.adj[v].append(w)

    def BFS(self, n):
        visited = [False] * self.node
        que = deque()
        que.append(n)
        visited[n] = True

        while que:
            n = que.popleft()
            print(n, end=" ")

            for a in self.adj[n]:
                if not visited[a]:
                    visited[a] = True
                    que.append(a)


graph = BFSTraversal(6)
graph.insertEdge(0, 1)
graph.insertEdge(0, 3)
graph.insertEdge(0, 4)
graph.insertEdge(4, 5)
graph.insertEdge(3, 5)
graph.insertEdge(1, 2)
graph.insertEdge(1, 0)
graph.insertEdge(2, 1)
graph.insertEdge(4, 1)
graph.insertEdge(3, 1)
graph.insertEdge(5, 4)
graph.insertEdge(5, 3)

print("Breadth First Traversal for the graph is:")
graph.BFS(0)

