import heapq
from collections import defaultdict
import sys


# class Graph
class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

# hendler
def dijkstra(graph, start):
    # init
    distances = {node: float('inf') for node in graph.edges}
    distances[start] = 0
    # turn with priority with initialization of the initial vertex
    priority_queue = [(0, start)]  

    while priority_queue:
        # We choose the top with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        # If the current distance is greater than already found, we miss
        if current_distance > distances[current_node]:
            continue
        # We review the neighbors of the current vertex
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            # Update the distance if found a shorter way
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


# Main
if __name__ == '__main__':
    # case
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 1)
    graph.add_edge('C', 'B', 2)
    graph.add_edge('C', 'D', 5)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('D', 'E', 3)
    # start from A point 
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print("The shortest distances from the top", start_node, ":", distances)
