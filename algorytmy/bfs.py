from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search algorithm.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
    
    Returns:
        List of vertices in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# Example usage
if __name__ == "__main__":
    # Sample graph represented as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    
    print("BFS starting from vertex 0:")
    print(bfs(graph, 0))
