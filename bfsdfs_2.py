#Recursive dfs (depth-first search)
def dfs_recursive(graph,vertex,visited):
    #mark the vertex as visited
    visited.add(vertex)
    print(vertex,end=" ") #visit the current vertex
    
    #recursively visit all unvisited neighbours 
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)
            
    
#Recursively bfs(breadth-first search)
def bfs_recursive(graph,queue,visited):
    if not queue:
        return
    
    vertex = queue.pop(0) # Dequeue the first vertex in the queue
    if vertex not in visited:
        visited.add(vertex)
        print(vertex,end=" ") #visit the current vertex
        
    # Enqueue all unvisited neighbors
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            
    # Recursively call to process the next level
    bfs_recursive(graph, queue, visited)
    

#Recursive bfs starting function
def recursive_bfs(graph,start_vertex):
    visited = set() ## Initialize visited set
    queue = [start_vertex] # Initialize queue with the starting vertex
    bfs_recursive(graph, queue, visited)
    
# Example of an undirected graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

#bfs traversal (Recursive)
print("Recursive DFS Traversal :")
visited_dfs = set()
dfs_recursive(graph, 0, visited_dfs)  # Starting DFS traversal from vertex 0
print("\n")

# BFS Traversal (Recursive)
print("Recursive BFS Traversal:")
recursive_bfs(graph, 0)  # Starting BFS traversal from vertex 0
print("\n")