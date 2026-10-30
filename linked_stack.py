class Node:
def init(self, data):
self.data = data
self.next = None

class LinkedStack:
def init(self):
self.head = None
self.size = 0

def is_empty(self):
    return self.head is None

def is_full(self):
    return False

def push(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

def pop(self):
    if self.is_empty():
        raise IndexError("Stack underflow: stack is empty.")
    item = self.head.data
    self.head = self.head.next
    self.size -= 1
    return item

def peek(self):
    if self.is_empty():
        raise IndexError("Stack is empty.")
    return self.head.data

def __str__(self):
    items = []
    current = self.head
    while current:
        items.append(current.data)
        current = current.next
    return str(items)
