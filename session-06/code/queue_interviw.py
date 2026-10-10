# Given a queue of integers, 
# reverse its elements using a stack.

# Input: [10, 20, 30, 40]
# Output: [40, 30, 20, 10]


from collections import deque

def reverse_queue(queue):
    stack = []

    # step 1 : remove elements from the front of the queue
    while queue:
        stack.append(queue.popleft())

    # step 2 : the stack returns elements in the reverse order
    # add them back to the rear of the queue
    while stack:
        queue.append(stack.pop())

    return queue


# time complexity
# The time complexity of this algorithm is O(n),
#  where n is the number of elements in the queue.


# test the reverse_queue function
if __name__ == "__main__":
    q = deque([10, 20, 30, 40])
    print("Original queue:", list(q))
    reversed_q = reverse_queue(q)
    print("Reversed queue:", list(reversed_q))


# Given a positive integer n, 
# generate the binary representations of
# every number from 1 to n using a queue.

# examples 
# input : n = 5
# output : ['1', '10', '11', '100', '101']  
# means you have to generate the binary representations of
# every number from 1 to n using a queue.
# Approach
# 1. Initialize a queue and enqueue the first binary number "1".
# 2. For each number from 1 to n, do the following:
#    a. Dequeue the front element.
#    b. Generate the next two binary numbers by appending "0" and "1" to the current number.
#    c. Enqueue the new binary numbers.
# 3. Continue this process until you have generated all binary numbers up to n.



def generate_binary_numbers(n):
    queue = deque()
    result = []

    # Step 1: Enqueue the first binary number "1"
    queue.append("1")

    # Step 2: Generate binary numbers from 1 to n
    for _ in range(n):
        # a. Dequeue the front element
        current = queue.popleft()
        result.append(current)

        # b. Generate the next two binary numbers
        queue.append(current + "0")
        queue.append(current + "1")

    return result


# test it
print(generate_binary_numbers(9))  # Should print ['1', '10', '11', '100', '101']


# Given a queue and an integer k, reverse the first k
# elements while keeping the remaining elements in their original order.

# Input: Queue = [10, 20, 30, 40, 50], k = 3
# Output: [30, 20, 10, 40, 50]

# example 2
# Input: Queue = [1, 2, 3, 4, 5], k = 2
# Output: [2, 1, 3, 4, 5]

# examples 3
# Input: Queue = [5, 4, 3, 2, 1], k = 5
# Output: [1, 2, 3, 4, 5]


# some edge cases
# Input: Queue = [10, 20, 30], k = 5
# Output: [30, 20, 10]

# Input: Queue = [], k = 3
# Output: []

# Input: Queue = [1, 2, 3], k = 0
# Output: [1, 2, 3]