graph = {
    "Oradea": ({"Zerind": 71, "Sibiu": 151}, 380),
    "Zerind": ({"Oradea": 71, "Arad": 75}, 374),
    "Arad": ({"Zerind": 75, "Sibiu": 140, "Timisoara": 118}, 399),
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
graph = {
    "per1": ({"per2": 10, "per3": 15, "per4": 30}, 25),  
    "per2": ({"per1": 10, "per4": 12, "per5": 35}, 20),  
    "per3": ({"per1": 15, "per5": 20}, 30),                  
    "per4": ({"per2": 12, "per1": 30, "per6": 17}, 15),    
    "per5": ({"per3": 20, "per2": 35, "per6": 14}, 10),          
    "per6": ({"per4": 17, "per5": 14}, 0)
}

def greedy_search_rec(graph, prev, dst, path, q):
    # n: (h(n))
    print("Connected nodes of current node", prev, "with h(n) values:")
    
    # Explore neighboring nodes and add them to the queue with their heuristic values
    for n in graph[prev][0]:
        if n not in path:  # Avoid cycles by not revisiting nodes in the current path
            q[n] = graph[n][1]  # Add node with its heuristic value
            print(n, "->", q[n])
    
    while q:
        # Find the node with the minimum heuristic value
        mn = min(q, key=q.get)
        print("Taking minimum h(n) vertex:", mn)
        
        if dst == mn:
            return path + [dst]  # Destination found
        
        # Remove the current minimum from the queue
        del q[mn]
        
        # Recursive call for the node with the minimum heuristic value
        new_path = greedy_search_rec(graph, mn, dst, path + [mn], q)
        
        # If a valid path is found in the recursive call, return it
        if new_path:
            return new_path
    
    return []  # No path found, return an empty list

# User inputs
source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")

# Call the greedy search function
path = greedy_search_rec(graph, source, dest, [source], {})

# Output the result
if path:
    print("Path found:", path)
else:
    print("Path not found!!")
