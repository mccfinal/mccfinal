adj_list = {
    'A' : ['B','C','D'],
    'B' : ['E'],
    'C' : ['F','G'],
    'D' : ['C'],
    'E' : ['H','F'],
    'F' : ['B'],
    'H' : [],
    'G' : [],
}

def dls(s, g, path, level, max_depth):
    print("Current Level:", level)
    print(f"Testing node {s} for goal {g}")
    
    path.append(s)

    if level > max_depth:
        print("Max depth limit reached")
        path.pop()  # remove the current node from path before returning
        return False
    
    if s == g:
        print("Goal node found!")
        return True
    
    print(f"Expanding node {s}")
    print("------------------------")
    
    for neighbor in adj_list[s]:
        if neighbor not in path:  # Prevent cycles by checking if already in path
            if dls(neighbor, g, path, level + 1, max_depth):
                return True
    
    # If no path is found from this node, backtrack
    path.pop()
    return False

# User inputs
s = input("Enter Source node: ")
g = input("Enter the goal node: ")
max_depth = int(input("Enter Maximum depth limit: "))

print()
path = []
if dls(s, g, path, 0, max_depth):
    print("There exists a path from source to goal.")
    print("Path is:", " -> ".join(path))
else:
    print("No path from source to goal within the given depth limit.")
