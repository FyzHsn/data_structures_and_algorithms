class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()

    def add_child(self, key):
        if not isinstance(key, Node):
            self.children[key] = Node(key)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]


class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]    

    def add(self, word):
        current_node = self.head
        word_finished = True
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break
        if not word_finished:
            while i < len(word):
                current_node.add_child(word[i])
                current_node = current_node.children[word[i]]
                i += 1
        current_node.data = word

    def search(self, word):
        found_word = False
        current_node = self.head
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                return found_word
        if current_node.data == word:
            found_word = True
        return found_word    

    def get_words(self, prefix=''):
        words = list()
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                return words
                  
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]

        while queue != []:
            current_node = queue.pop(0)
            for key, node in current_node.children.items():
                queue.append(node)
                if node.data:
                    words.append(node.data)

        return words

if __name__ == "__main__":
    n = Node('a')
    n.add_child('e')
    n.add_child('e')
    n.add_child('u')
    print(n.children)
    n['e'].add_child('x')
    print(n['e'].children)
        
    t = Trie()
    t.add('mango')
    t.add('men')
    t.add('mat')
    t.add('apples')
    t.add('apple')
    print(t.search('more'))
    print(t.search('mango'))
 
    print(t.get_words())












    
