class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
        
    def peek(self):   
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def to_list(self):
        return self.items.copy()
    
    def from_list(self, lst):
        self.items = lst.copy()
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)
print(s.peek())      
print(s.pop())       
print(s.items)       
print(s.is_empty())

# =========================
# Part 1 — Stack Class (List-based)
# =========================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


    # =========================
    # Part 2 — Stack Applications
    # =========================

    # 1. Reverse a string using a stack
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

        reversed_str = ""
        while not stack.is_empty():
            reversed_str += stack.pop()

            return reversed_str


        # 2. Check if parentheses are balanced
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in pairs.values():  # opening brackets
            stack.push(char)
        elif char in pairs.keys():  # closing brackets
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

            return stack.is_empty()


            # 3. Simulate an undo system
def undo_system(actions):
    stack = Stack()

    for action in actions:
        if action == "UNDO":
            if not stack.is_empty():
                stack.pop()
            else:
                stack.push(action)

                # Return remaining actions
                result = []
                while not stack.is_empty():
                    result.append(stack.pop())

                    return result[::-1]  # reverse to maintain original order


                # =========================
                # Part 3 — Linked List Stack
                # =========================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        removed = self.top
        self.top = self.top.next
        self._size -= 1
        return removed.value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


    # =========================
    # Part 4 — Short Answers
    # =========================

    # 1. Why are push and pop O(1) in a stack?
    # Push and pop are O(1) because they only add or remove an element
    # from the top of the stack without needing to shift or traverse
    # other elements.

    # 2. What makes a stack different from a queue?
    # A stack follows LIFO (Last In, First Out), meaning the last element
    # added is the first to be removed.
    # A queue follows FIFO (First In, First Out), meaning the first element
    # added is the first to be removed.

    # 3. Name two real-world systems that use stack behavior.
    # - Undo/Redo functionality in text editors
    # - Browser history (back button navigation)


    # =========================
    # Example Usage (Optional)
    # =========================

if __name__ == "__main__":
    print(reverse_string("hello"))  # "olleh"
    print(is_balanced("(a + b) * [c - d]"))  # True
    print(undo_system(["type A", "type B", "UNDO", "type C"]))
    # Output: ['type A', 'type C']