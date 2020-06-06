from collections import deque


def print_binary_numbers(n):
    q = deque()
    q.append('1')

    while n > 0:
        n -= 1
        
        temp = q.popleft()
        q.append(temp + '0')
        q.append(temp + '1')
        
        print(temp)
    
if __name__ == "__main__":
    print_binary_numbers(4)
