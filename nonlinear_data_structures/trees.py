'''
Input:
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
               \
                8
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"node: {self.value}, left: {self.left}, right: {self.right}"


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print(self._preorder_print(self.root)) 
        elif traversal_type == "inorder":
            print(self._inorder_print(self.root))

        elif traversal_type == "postorder":
            print(self._postorder_print(self.root))

    def _preorder_print(self, start, traversal=""):
        '''Root -> Left -> Right'''

        if start is not None:
            traversal += f'{str(start.value)}-'
            traversal = self._preorder_print(start.left, traversal)
            traversal = self._preorder_print(start.right, traversal)

        return traversal

    def _inorder_print(self, start, traversal=""):
         '''Left -> Root -> Right'''
    
         if start is not None:
            traversal = self._inorder_print(start.left, traversal)
            traversal += f'{str(start.value)}-'
            traversal = self._inorder_print(start.right, traversal)

         return traversal
            
    def _postorder_print(self, start, traversal=""):
         '''Left -> Right -> Root'''
    
         if start is not None:
            traversal = self._inorder_print(start.left, traversal)
            traversal = self._inorder_print(start.right, traversal)
            traversal += f'{str(start.value)}-'

         return traversal
        

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)

    tree.print_tree("preorder")
    tree.print_tree("inorder")
    tree.print_tree("postorder")
