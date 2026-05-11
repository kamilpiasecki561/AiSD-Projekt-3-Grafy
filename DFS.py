def dfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    stack = [start]  # Stack for DFS

    while stack:
        node = stack.pop()  # Get the last node from the stack
        if node not in visited:
            print(node)  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited

            # Add all unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)