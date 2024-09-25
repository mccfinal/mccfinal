graph = {
    "Oradea": ({"Zerind": 71, "Sibiu": 151}, 380),
    "Zerind": ({"Oradea": 71, "Arad": 75}, 374),
    "Arad": ({"Zerind": 75, "Sibiu": 140 , "Timisoara": 118}, 399),
    "Timisoara": ({"Arad": 118, "Lugoj": 111}, 329),
    "Lugoj": ({"Timisoara": 111, "Mehadia": 70}, 244),
    "Mehadia": ({"Lugoj": 70, "Drobeta": 75}, 241),
    "Sibiu": ({"Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80, "Arad": 140}, 253),
    "Fagaras": ({"Sibiu": 99, "Bucharest": 211}, 176),
    "Rimnicu Vilcea": ({"Sibiu": 80, "Pitesti": 97, "Craiova": 146}, 193),
    "Bucharest": ({"Fagaras": 211, "Pitesti": 101, "Urziceni": 85, "Giurgiu": 90}, 0),
    "Pitesti": ({"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101}, 100),
    "Craiova": ({"Rimnicu Vilcea": 146, "Pitesti": 138, "Drobeta": 120}, 160),
    "Drobeta": ({"Mehadia": 75, "Craiova": 120}, 242),
    "Urziceni": ({"Bucharest": 85, "Vaslui": 142, "Hirsova": 98}, 80),
    "Giurgiu": ({"Bucharest": 90}, 77),
    "Vaslui": ({"Iasi": 92, "Urziceni": 142}, 199),
    "Hirsova": ({"Urziceni": 98, "Eforie": 86}, 151),
    "Iasi": ({"Vaslui": 92, "Neamt": 87}, 226),
    "Eforie": ({"Hirsova": 86}, 161),
    "Neamt": ({"Iasi": 87}, 234)
}

def get_min(q):
    """Helper function to get the node with the minimum A* cost (f = g + h)."""
    mn = (None, (0, float("INF")))  # Initialize with infinity
    for i in q:
        if sum(q[i]) < sum(mn[1]):  # Compare based on f(n) = g(n) + h(n)
            mn = (i, q[i])
    return mn[0]

def a_star(graph, prev, dst, path, pcost, q):
    print(f"Connected nodes of current node {prev} with heuristic and path costs:")
    
    # Explore the neighbors of the current node
    for n in graph[prev][0]:  # neighbors with distances
        if n not in path:  # Only consider unexplored nodes
            g_cost = pcost + graph[prev][0][n]  # g(n): actual cost from start
            h_cost = graph[n][1]  # h(n): heuristic to destination
            q[n] = (h_cost, g_cost)
            print(f"{n} -> (heuristic: {h_cost}, path cost: {g_cost})")
    
    # Process the node with the minimum f(n) = g(n) + h(n)
    while q:
        mn = get_min(q)
        print(f"Selecting node with minimum A* value: {mn}")
        print("__________________________________________________")
        
        # If the destination is found, return the path
        if dst == mn:
            return path + [dst]
        
        # Update path cost (g(n)) for the selected node
        pc = q[mn][1]
        print(f"Current path cost: {pc}")
        
        # Remove the selected node from the queue
        del q[mn]
        
        # Recursively search for the destination from the selected node
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    
    return []  # Return empty if no path is found

# Input source and destination
source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")

# Check if source and destination exist in the graph
if source in graph and dest in graph:
    heuristic = graph[source][1]  # Start with the heuristic of the source node
    path = a_star(graph, source, dest, [], 0, {source: (heuristic, 0)})
    if path:
        print(f"Path found: {path}")
    else:
        print("Path not found")
else:
    print("Invalid source or destination node!")
