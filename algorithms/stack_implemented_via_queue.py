from collections import deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.popleft()   

    def top(self):
        if not self.items:
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = Queue()

    def push(self, item):        
        self.items.enqueue(item)
        for _ in range(len(self.items) - 1):
            dequeued = self.items.dequeue()
            self.items.enqueue(dequeued)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.dequeue()

    
if __name__ == "__main__":
    s = Stack()
    l = [1, 2, 3, 4]
    for element in l:
        s.push(element)
    for _ in range(len(l)):
        print(s.pop())
