# Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, x):
        # Alway 0(1)
        self.in_stack.append(x)
        
    def dequeue(self):
        if not self.out_stack:
            # Transfer only when needed
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
        if not self.out_stack:
            raise IndexError("Queue is empty")
        
        return self.out_stack.pop()
    
    def is_empty(self):
        return not self.in_stack and not self.out_stack
    
# Reverse a Queue using a Stack

from collections import deque

def reverse_queue(q):
    stack = []
    
    # Step 1: Move queue -> stack
    while q:
        stack.append(q.popleft())
        
    # Step 2: Move stack -> queue
    while stack:
        q.append(stack.pop())
        
    return q

# Generate First N Binary Numbers Using a Queue

from collections import deque

def generate_binary_numbers(n):
    result = []
    q = deque()

    q.append("1")

    for _ in range(n):
        current = q.popleft()
        result.append(current)

        q.append(current + "0")
        q.append(current + "1")

        return result
    
print(generate_binary_numbers(5))