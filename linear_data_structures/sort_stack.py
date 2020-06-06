from collections import deque


def insert_at_bottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return

    temp = stack.pop()
    print("after pop")    
    print(stack)
    insert_at_bottom(stack, element)
    print("after insert")
    print(stack)
    stack.append(temp)


def reverse_stack(stack):
    if len(stack) == 0:
        return stack

    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

    return stack





def sorted_insert(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element) 

    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.append(temp)

    return stack


def sort_stack(stack):
    if len(stack) == 0:
        return stack  

    temp = stack.pop()
    sort_stack(stack)
    return sorted_insert(stack, temp)

if __name__ == "__main__":
    s = deque()
    for element in [30, -5, 18, 14, -3]:
        s.append(element) 

    print(sort_stack(s))

    print(reverse_stack(s))
