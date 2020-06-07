from collections import deque


def generate_binary_numbers(n):
    """Time Complexity: O(n), Auxilary space Complexity: O(n)"""

    counter = 1
    queue = deque(['1'])
    while counter < n:
        temp = queue.popleft()
        yield temp
        queue.append(temp + '0')
        queue.append(temp + '1')
        counter += 1
       

if __name__ == "__main__":
    print(list(generate_binary_numbers(10)))
