from collections import deque


def recursive_dfs(graph, start, stack=None):
    if stack is None:
        stack = deque([start])

    path = stack.pop()
    cur_node = path[-1]
    adj_nodes = graph[cur_node]
    
    if len(adj_nodes) == 0:
        yield path

    for node in adj_nodes:
        if node not in path:
            stack.append(path + node)
        else:
            yield path

    if len(stack) != 0:
        yield from recursive_dfs(graph, start, stack)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['D', 'E'],
             'C': ['F'],
             'D': [],
             'E': ['F'],
             'F': []}

print(list(recursive_dfs(graph, 'A')))

