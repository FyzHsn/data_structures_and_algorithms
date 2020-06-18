def dijkstra(graph, start, goal):
    """Time complexity: O(), Auxiliary space complexity: O()"""

    shortest_dist = {}
    predecessor = {}
    unseen_nodes = graph
    infty = 9999999999999999
    path = []

    shortest_dist = {node: infty for node in unseen_nodes}
    shortest_dist[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_dist[node] < shortest_dist[min_node]:
                min_node = node
        
        for child_node, weight in graph[min_node].items():
            if weight + shortest_dist[min_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight + shortest_dist[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)
    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print("path cannot be reached")
            break
    path.insert(0, start)
    if shortest_dist[goal] != infty:
        print(str(path))
    
    return shortest_dist
    

if __name__ == "__main__":
    g = {'a': {'b': 10, 'c': 3}, 
         'b': {'c': 1, 'd': 2},
         'c': {'b': 4, 'd': 8, 'e': 2},
         'd': {'e': 7},
         'e': {'d': 9}} 

    print(dijkstra(g, 'a', 'd'))
