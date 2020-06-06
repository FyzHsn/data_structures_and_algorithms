from collections import deque


def bfs(graph, start, end):
    visited = []
    queue = deque([start])

    while len(queue) != 0:
        current = queue.popleft()
        for node in graph[current[-1]]:
            queue.append(current + node)
            if node == end:
                return current + node
    return None


def recursive_bfs(graph, start, queue=None):
    if queue is None:
        queue = deque([start])

    path = queue.popleft()
    cur_node = path[-1]
    adj_nodes = graph[cur_node]
    if adj_nodes == []:
        yield path
 
    for adj_node in adj_nodes:
        if adj_node not in path:
            queue.append(path + adj_node)
        else:
            yield path
         
    if len(queue) != 0:
        yield from recursive_bfs(graph, start, queue)


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['D', 'E'],
             'C': ['F'],
             'D': [],
             'E': ['F'],
             'F': []}

    print(bfs(graph, 'A', 'L'))

    for path in recursive_bfs(graph, 'A'):
        print(path)
      
