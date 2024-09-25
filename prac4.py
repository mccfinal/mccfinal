graph = {
    "M": ["N", "Q", "R"],
    "N": ["O", "Q", "M"],
    "R": ["M"],
    "O": ["P", "N"],
    "Q": ["M", "N", "P"],
    "P": ["O", "Q"]
}

def DFS(curNode, destination, graph, maxDepth):
    print("Checking for destination ", curNode)

    if curNode == destination:
        print("Goal Found")
        return True
    if maxDepth <= 0:
        return False
    for node in graph[curNode]:
        if DFS(node, destination, graph, maxDepth - 1):
            return True
    return False

def iterativeDDFS(curNode, destination, graph, maxDepth):
    for i in range(maxDepth + 1):  # Iterate from depth 0 to maxDepth
        print(f"Depth limit: {i}")
        if DFS(curNode, destination, graph, i):
            return True
    return False

M = input("enter source node")
P = input("enter destination node")

if not iterativeDDFS(M, P, graph, 3):
    print("Path is Not Available")
else:
    print("A path exists")
