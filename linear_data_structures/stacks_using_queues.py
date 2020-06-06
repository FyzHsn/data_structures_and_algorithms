class Queue:
    def __init__(self, l=[]):
        self.items = l
        self.size = len(l)

    def is_empty(self):
        return self.size == 0 

    def enqueue(self, item):
        self.items.append(item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

    def top(self):
        return self.items[-1]

    def print(self):
        print(self.items)

class Stack:
    def __init__(self, l=[]):
        self.queue = Queue(l)

    def is_empty(self):
        return self.queue.is_empty

    def push(self, item):
        self.queue.enqueue(item)

    def pop(self):
        for _ in range(0, self.queue.size - 1):
            dequeued = self.queue.dequeue()
            self.queue.enqueue(dequeued)

        return self.queue.dequeue()
    

def reverse_queue(q, k):
    s = []

    

    
    return q


if __name__ == "__main__":
    q = Queue()
    l = [1, 2, 3, 4, 5]
    for element in l:
        q.enqueue(element)

    new_q = reverse_queue(q, 3)
    for i in range(0, new_q.size):
        print(new_q.dequeue())


