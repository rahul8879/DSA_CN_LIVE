class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        # here we will initialize the stack with a linked list
        # here first will point to the top of the stack and last will point to the bottom of the stack
        self.first = None
        self.last = None
        self.size = 0

    def addAtBeginning(self, value):
        new_node = Node(value)
        if not self.first:  # If the stack is empty
            self.first = new_node
            self.last = new_node

        else:
            temp = self.first
            self.first = new_node
            self.first.next = temp
        self.size += 1
        return self
    

    def removeFromBeginning(self):
        if not self.first:  # If the stack is empty
            return None
        removed_value = self.first.value
        self.first = self.first.next
        self.size -= 1
        return removed_value


# lets test our stack implementation
stack = StackLinkedList()
stack.addAtBeginning(10)
stack.addAtBeginning(20)
stack.addAtBeginning(30)
print(stack.removeFromBeginning())  # Should print 30
print(stack.removeFromBeginning())  # Should print 20
print(stack.removeFromBeginning())  # Should print 10
print(stack.removeFromBeginning())  # Should print None