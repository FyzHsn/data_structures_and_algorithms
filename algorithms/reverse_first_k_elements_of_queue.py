from collections import deque


def reverse(q):
    if not q:
        return 
    dequeued = q.popleft()
    reverse(q)
    q.append(dequeued)


def reverse_first_k(q, k):
    reverse(q)
    stack = deque()
    for _ in range(len(q) - k):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q


if __name__ == "__main__":
    queue = deque([1, 2, 3, 4, 5])
    reversed = reverse_first_k(queue, 3)
    while reversed:
        print(reversed.popleft())
