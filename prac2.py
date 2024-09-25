# Adjacency list
adj_list = {
    'A': ['C', 'D', 'B'],
    'C': ['A', 'K'],
    'D': ['A', 'K', 'L'],
    'K': ['C', 'D', 'L'],
    'L': ['K', 'D', 'J'],
    'J': ['M'],
    'B': ['A'],
    'M': ['J']
}

# Initialization
visited = {}
level = {}
parent = {}
dfs_traversal = []
stack = []

# Initialize visited, parent, and level dictionaries
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

source = input("Enter the exact Source node: ")
visited[source] = True
level[source] = 0
stack.append(source)

# DFS traversal using stack
while stack:
    u = stack.pop()
    dfs_traversal.append(u)
    
    # Visit all adjacent nodes of u
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            stack.append(v)  # Push adjacent node to the stack for DFS

print("DFS traversal:", dfs_traversal)

# Minimum path using parent pointers
target = input("Enter the exact node to reach: ")  # Destination node
path = []

if visited[target]:  # If the target node is reachable
    node = target
    while node is not None:  # Backtrack from the target to the source
        path.append(node)
        node = parent[node]
    path.reverse()  # Reverse the path to get it from source to target

if path:
    print("Minimum path from Source to Destination:", ' -> '.join(path))
else:
    print("No path found from Source to Destination.")
