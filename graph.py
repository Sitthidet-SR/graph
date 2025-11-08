class Vertex:
    def __init__(self, end):
        self.end = end
        self.next = None

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
class Graph:
    def __init__(self, v):
        self.point = [None] * v
def create_graph(edges, x, v):
        graph = Graph(v)
        for i in range(v):
            graph.point[i] = None
        
        for i in range(x):
            start = edges[i].start
            end = edges[i].end
            
            vertex = Vertex(end)
            vertex.next = graph.point[start]
            graph.point[start] = vertex

        return graph

# รับค่า input
v = int(input("Enter number of vertex: "))
n = int(input("Enter number of edges: "))

edges = []
print("Enter edges (start end):")
for i in range(n):
    start, end = map(int, input().split())
    edges.append(Edge(start, end))

graph = create_graph(edges, n, v)

print("\nGraph created is:")
for i in range(v):
    ptr = graph.point[i]
    while ptr is not None:
        print("( {} -> {})".format(i, ptr.end), end="\t")
        ptr = ptr.next
    print()