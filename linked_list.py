# Part 1 — Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            curr.next = new_node

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
            return count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            return slow.value if slow else None

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
            return result
        
self = SinglyLinkedList()
for val in [1, 2, 3, 4, 5]:
    self.append(val)
print("Original list:", self.to_list())
print("Length:", self.length())

        
# Part 2 — Doubly Linked List

class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_tail(self, value):
        new_node = DoublyNode(value)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_value(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                    if curr.next:
                        curr.next.prev = curr.prev
                    else:
                        self.tail = curr.prev
                        return
                    curr = curr.next

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
            return result

    def to_list_reversed(self):
        result = []
        curr = self.tail
        while curr:
            result.append(curr.value)
            curr = curr.prev
            return result

dll = DoublyLinkedList()
for val in [1, 2, 3, 4, 5]:
    dll.insert_tail(val)
print("Original list:", dll.to_list())  
print("Reversed list:", dll.to_list_reversed())

      
# Part 3 — Circular Linked List
        

class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = CircularNode(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

            curr.next = new_node
            new_node.next = self.head

    def delete_value(self, value):
        if not self.head:
            return

        curr = self.head
        prev = None

        while True:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    # deleting head
                    if curr.next == self.head:
                        self.head = None
                        return
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                        self.head = curr.next
                        tail.next = self.head
                        return

                    prev = curr
                    curr = curr.next
                    if curr == self.head:
                        break

    def print_list(self, steps):
        result = []
        curr = self.head
        for _ in range(steps):
            if not curr:
                break
            result.append(curr.value)
            curr = curr.next
            return result


            # Demonstration: cycle twice
        cll = CircularLinkedList()
        for val in [1, 2, 3, 4]:
            cll.insert(val)

            cycle_demo = cll.print_list(8)  # twice the list size
            print("Cycle twice:", cycle_demo)


"""
Part 4 — Short Answers
                

1. When would you prefer a doubly linked list?
    a. You prefer a doubly linked list when you need to traverse in both directions (forward and backward) or when deleting nodes frequently, since you can use the prev pointer without needing to track the previous node manually.

2. Real-world scenario for circular linked list:
    a. A music playlist that loops continuously, where after the last song,
    b. it automatically returns to the first song.

3. Main trade-off between linked lists and arrays:
    a. Linked lists allow dynamic size and efficient insertions/deletions, but arrays provide faster indexing (O(1)) and better memory locality.
"""
                
                
