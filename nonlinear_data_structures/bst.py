class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, cur_node, data):
        if data < cur_node.data:
            if not cur_node.left:
                cur_node.left = Node(data)
            else:
                self._insert(cur_node.left, data)
        elif data > cur_node.data:
            if not cur_node.right:    
                cur_node.right = Node(data)
            else:
                 self._insert(cur_node.right, data)

        else:
            print("Value is already present in tree")

    def search(self, data):
        if self.root is not None:
            is_found = self._search(self.root, data)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _search(self, cur_node, data):
        if data < cur_node.data and cur_node.left:
            return self._search(cur_node.left, data)
        elif data > cur_node.data and cur_node.right:
            return self._search(cur_node.right, data)
        elif cur_node.data == data:
            return True
        

if __name__ == "__main__":
    bst = BST()
    bst.insert(4)
    bst.insert(1)
    bst.insert(10)
    bst.insert(11)
    bst.insert(2)
    print(bst.search(3))
    print(bst.search(11))
     
        
