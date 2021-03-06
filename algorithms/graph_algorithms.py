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
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    queue = deque([start])
    while len(queue) > 0:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph[node]:
            if neighbor == end:
                return path + neighbor
            elif neighbor not in path and neighbor != end:
                queue.append(path + neighbor)
    return None


def get_edge_num(graph):
    """Time Complexity: O(V), Auxiliary Space Complexity: O(1)"""

    edge_num = 0
    for node, neighbors in graph.items():
        edge_num += len(neighbors) 
    return edge_num / 2


def count_incoming_outgoing_edges(graph):
    """Time Complexity: O(V*E), Auxiliary Space Complexity: O(V)"""
   
    incoming_dict = dict() 
    outgoing_dict = dict()
    for node in graph:
        outgoing_dict[node] = len(graph[node])
        for neighbor in graph[node]:
            if neighbor in incoming_dict:
                incoming_dict[neighbor] += 1
            else:
                incoming_dict[neighbor] = 1
    return incoming_dict, outgoing_dict


def find_root_node(graph):
    """Time Complexity: O(V), Auxiliary Space Complexity: O(V)"""
   
    incoming_dict, outgoing_dict = count_incoming_outgoing_edges(graph)
    candidates = []
    for node in outgoing_dict:
        if node not in incoming_dict:
            candidates.append(node)
    if len(candidates) == 1:
        return candidates[0]
    return None 


def is_graph_acyclic(graph): 
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    not_visited = set(graph.keys())
    visited = set()
    while len(not_visited) > 0:
        start = not_visited.pop()
        queue = deque([start])
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    return False
                else:
                    visited.add(neighbor)
                    queue.append(neighbor)
        not_visited = not_visited - visited
        visited = set()
    return True


def is_graph_tree(graph):
    """Time Complexity: O(V + E), Auxiliary Space Complexity: O(V + E)"""

    if find_root_node(graph) and is_graph_acyclic(graph):
        return True    


def find_disjoint_nodes(graph):
    "Time Complexity: O(???), Auxiliary Space Complexity: O(???)"""

    sets_by_element_dict = {}
    
    def make_new_set_for(x, y):
        sets_by_element_dict[x] = sets_by_element_dict[y] = set({x, y})

    def add_element_to_set(s, e):
        s.add(e)
        sets_by_element_dict[e] = s

    def merge_sets(s_1, s_2):
        merged_set = s_1.union(s_2)
        for e in merged_set:
            sets_by_element_dict[e] = merged_set

    for node_1 in graph:
        for node_2 in graph[node_1]:
            node_1_set = sets_by_element_dict.get(node_1)
            node_2_set = sets_by_element_dict.get(node_2)

            if node_1_set is None and node_2_set is None:
                make_new_set_for(node_1, node_2)

            if node_1_set is None and node_2_set is not None:
                add_element_to_set(node_2_set, node_1)

            if node_1_set is not None and node_2_set is None:
                add_element_to_set(node_1_set, node_2)

            if node_1_set is not None and node_2_set is not None and node_1_set != node_2_set:
                merge_sets(node_1_set, node_2_set)
    return  set(tuple(s) for s in sets_by_element_dict.values())


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

    print(find_shortest_path(g, "a", "f"))
    print(get_edge_num(g))

    t = {"a": ["b", "c"],
         "b": ["d", "e"],
         "c": ["f"],
         "d": [],
         "e": [],
         "f": []}
    print(find_root_node(t))
    print(find_root_node(g))
    print(is_graph_acyclic(t))

    c = {"a": ["b"],
         "b": ["a", "c"],
         "c": ["a", "b"],
         "e": ["f"],
         "f": ["e"],
        }
    print(is_graph_acyclic(c))
    print(find_disjoint_nodes(c))
    print(find_disjoint_nodes(g))
