class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def enqueue(self, elem):
        self.data.append(elem)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    def top(self):
        if self.is_empty():
            return None
        return self.items[0]

    def __repr__(self):
        return str(self.data[::-1])

if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q.is_empty())
    print(q)
        
