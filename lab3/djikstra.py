import heapq

def dijkstra(graph, start):
    priority_queue = [(0, start)]
    shortest_paths = {start: (None, 0)}
    
    while priority_queue:
        (current_distance, current_vertex) = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_vertex, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

for vertex in shortest_paths:
    print(f"Shortest path to {vertex} is {shortest_paths[vertex][1]} through {shortest_paths[vertex][0]}")
