class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def insert_at_head(self, value):
        node = Node(value)
        if self.size == 0:
            self.tail = node
        else:
            node.next = self.head  
        self.head = node
        self.size += 1        
 
    def insert_at_tail(self, value):
        node = Node(value)        
        if self.size == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
   
    def delete_at_head(self):
        if self.head is not None:
            node = self.head.next
            self.head = node
            self.size -= 1
        if self.size == 0:
            self.tail = None

    def delete_at_tail(self):
        prev = None
        cur = self.head
        while cur is not None:
            if prev is None and cur.next is None:
                self.head = None
                self.tail = None
                cur = None
                self.size -= 1
            elif prev is not None and cur.next is None:
                prev.next = None
                self.tail = prev
                self.size -= 1
                cur = None
            else:
                prev = cur
                cur = cur.next        

    def delete(self, value):
        prev = None
        for cur in self:
            if prev is None and cur.value == value:
                self.head = cur.next
                cur.next = None
                self.size -= 1
            elif prev != None and cur.value == value:
                prev.next = cur.next
                cur.next = None
                self.size -= 1
            else:
                prev = cur
        if prev is None or prev.next is None:
            self.tail = prev

    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next 

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        return " -> ".join(nodes)

if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.delete_at_tail()
    print(ll.size)
    print(ll)
    # ll.delete(3)
    # ll.delete(2)
    # print(ll)
    # ll.delete_at_head()
    # print(ll)
    # ll.delete_at_head()
    # print(ll)
