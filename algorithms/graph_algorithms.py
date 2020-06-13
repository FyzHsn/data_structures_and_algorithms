from collections import deque


def depth_first_search(graph, start, end):
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    stack = deque([start])
    while len(stack) > 0:
        path = stack.pop()
        node = path[-1]
        for neighbor in graph[node]:
            if neighbor == end:
                yield path + neighbor
            elif neighbor not in path and neighbor != end:
                stack.append(path + neighbor)


def recursive_depth_first_search(graph, start, end, stack=None):
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    if stack is None:
        stack = deque([start])

    path = stack.pop()
    node = path[-1]
    for neighbor in graph[node]:
        if neighbor == end:
            yield path + neighbor
        elif neighbor not in path and neighbor != end:
            stack.append(path + neighbor)
            yield from recursive_depth_first_search(graph, start, end, stack) 


def breadth_first_search(graph, start, end):
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    queue = deque([start])
    while len(queue) > 0:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph[node]:
            if neighbor == end:
                yield path + neighbor
            elif neighbor not in path and neighbor != end:
                queue.append(path + neighbor)


def recursive_breadth_first_search(graph, start, end, queue=None):
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    if queue is None:
        queue = deque([start]) 

    path = queue.popleft()
    node = path[-1]
    for neighbor in graph[node]:
        if neighbor == end:
            yield path + neighbor
        elif neighbor not in path and neighbor != end:
            queue.append(path + neighbor)
            yield from recursive_breadth_first_search(graph, start, end, queue)
   

def find_shortest_path(graph, start, end):
    pass


def get_edge_num(graph):
    pass


def is_graph_tree(graph):
    pass


if __name__ == "__main__":
    g = { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]}
    print(list(depth_first_search(g, 'a', 'f')))
    print(list(recursive_depth_first_search(g, 'a', 'f')))

    print(list(breadth_first_search(g, 'a', 'f')))
    print(list(recursive_breadth_first_search(g, 'a', 'f')))

    
