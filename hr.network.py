def dfs(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited, graph)


# min operations required to connect all computers


def minOperations(comp_nodes, comp_from, comp_to):
    # Create a graph from the edges
    graph = {i: set() for i in range(1, comp_nodes + 1)}
    for f, t in zip(comp_from, comp_to):
        graph[f].add(t)
        graph[t].add(f)

    # Use DFS to find connected components
    visited = set()
    components = 0
    for node in range(1, comp_nodes + 1):
        if node not in visited:
            dfs(node, visited, graph)
            components += 1

    # If there's only one component then all computers are already connected
    if components == 1:
        return 0

    # If there are fewer than n-1 edges, it's not possible to connect all computers
    if len(comp_from) < comp_nodes - 1:
        return -1

    # Otherwise return the number of additional edges required to connect all components
    return components - 1


comp_nodes = 4
comp_from = [1, 2]
comp_to = [3, 4]
print(minOperations(comp_nodes, comp_from, comp_to))
