class ArrayQueue:
def init(self, capacity=5):
self.capacity = capacity
self.items = [None] * capacity
self.front = 0
self.size = 0

def is_empty(self):
    return self.size == 0

def is_full(self):
    return self.size == self.capacity

def enqueue(self, item):
    if self.is_full():
        raise OverflowError("Queue overflow: queue is full.")
    rear = (self.front + self.size) % self.capacity
    self.items[rear] = item
    self.size += 1

def dequeue(self):
    if self.is_empty():
        raise IndexError("Queue underflow: queue is empty.")
    item = self.items[self.front]
    self.items[self.front] = None
    self.front = (self.front + 1) % self.capacity
    self.size -= 1
    return item

def peek_front(self):
    if self.is_empty():
        raise IndexError("Queue is empty.")
    return self.items[self.front]

def __str__(self):
    result = []
    for i in range(self.size):
        index = (self.front + i) % self.capacity
        result.append(self.items[index])
    return str(result)
