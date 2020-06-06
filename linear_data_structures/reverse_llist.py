class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def add_first(self, node):
        node.next = self. head        
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
            
    def __repr__(self):
        node = self.head
        nodes = []
        prev_node_num = 0
        seen_all_nodes = False
        while node is not None and not seen_all_nodes:
            nodes.append(node.data)
            node = node.next

            if len(set(nodes)) == prev_node_num:
                seen_all_nodes = True

            prev_node_num = len(set(nodes))

        if not seen_all_nodes:
            nodes.append("None")
        else:
            nodes.append("...")

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove_duplicates(self):
        previous = None
        current = self.head
        seen = set()
        while current is not None:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = previous.next     


if __name__ == "__main__":
    llist = LinkedList(["a", "b", "c", "d", "b", "e", "a"])
    print(llist)
    llist.remove_duplicates()
    print(llist)













