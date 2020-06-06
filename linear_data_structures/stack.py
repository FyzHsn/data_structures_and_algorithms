class Stack:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def top(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None

    def is_empty(self):
        return self.data == []

    def __repr__(self):
        return str(self.data)



if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.top())
    print(s.is_empty())
    s.push(1) 
    print(s.top())
    print(s.is_empty())
    print(s)
    print(s.pop())
    print(s.pop())
    s.push(2)
    s.push(3)
    print(s)
    print(s.pop())
    

