# FIFO properties of queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:  # If the queue is empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self

    def dequeue(self):
        if not self.first:  # If the queue is empty
            return None
        removed_value = self.first.value
        self.first = self.first.next
        self.size -= 1
        return removed_value
    
# interview questions
# 1. How would you implement a queue using two stacks?
# 2. What are the time complexities of enqueue and dequeue operations in your implementation?
# 3. Can you implement a circular queue? What are the advantages of using a circular queue?