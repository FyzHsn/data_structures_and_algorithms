class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        """Time Complexity: O(1), Auxiliary Space Complexity: O(1)"""

        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head           
        self.size += 1

    def delete_at_head(self):
        """Time Complexity: O(1)"""

        if self.head is not None:
            self.head = self.head.next 

    def reverse(self):
        """Time Complexity: O(n), Auxiliary Space Complexity: O(1)"""
       
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
             temp = cur_node.next
             cur_node.next = prev_node
             prev_node = cur_node
             cur_node = temp
        self.head = prev_node

    def is_empty(self):
        """Time Complexity: O(n)"""

        if self.head is None:
            return True
        else:
            return False 

    def get_kth_node(self, k):
        """Time Complexity: O(n), Auxiliary Space Complexity: O(1)"""

        if self.head is None:
            return None
        counter = 0
        cur_node = self.head
        while cur_node is not None:
            if counter == k:
                return cur_node.data
            counter += 1
            cur_node = cur_node.next
        return None

    def get_kth_node_from_end(self, k):
        """Time Complexity: O(n), Auxiliary Space Complexity: O(1)"""

        m = self.size - k - 2
        if m < 0 or m > self.size - 1:
            return None
        return self.get_kth_node(m)

    def detect_loop(self):
        """Time Complexity: O(n), Auxiliary Space Complexity: O(n)"""

        visited_node_dict = dict()
        cur_node = self.head
        while cur_node is not None:
            if cur_node in visited_node_dict:
                return True
            visited_node_dict[cur_node] = True
            cur_node = cur_node.next
        return False

    def remove_duplicates(self):
        """Time Complexity: O(n), Auxiliary Space Complexity: O(n)"""

        duplicates_set = set()
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data in duplicates_set and cur_node.next is not None:
                prev_node.next = cur_node.next
                cur_node = cur_node.next
            elif cur_node.data in duplicates_set and cur_node.next is None:
                prev_node.next = None
                cur_node = None
            else:
                duplicates_set.add(cur_node.data)
                prev_node = cur_node
                cur_node = cur_node.next

    def __str__(self):
        nodes = []
        cur_node = self.head 
        while cur_node is not None:
            nodes.append(str(cur_node.data))
            temp = cur_node.next
            cur_node = temp
        return "->".join(nodes)
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(1)    
    ll.insert_at_head(2)    
    ll.insert_at_head(3)    
    ll.insert_at_head(34)    
    ll.insert_at_head(5)    
    ll.insert_at_head(3)    
    ll.insert_at_head(3) 
    print(str(ll))   
    ll.reverse()
    ll.delete_at_head()
    print(str(ll))
    print(ll.get_kth_node(3))
    print(ll.get_kth_node_from_end(0))
    print(ll.get_kth_node_from_end(2))
    # print(ll.detect_loop())
    # ll.head.next.next.next.next.next.next = ll.head.next.next
    # print(ll.detect_loop())
    ll.remove_duplicates()
    print(str(ll))
