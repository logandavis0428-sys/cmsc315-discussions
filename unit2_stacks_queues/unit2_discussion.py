
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding to the end ensures the last value added is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Return None if there are no values to remove.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the newest value without removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values go to the back, so the oldest values leave first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Return None when the queue is empty to avoid an error.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the oldest value without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Added 10, 20, 30, and 40 to the stack.")
    print("Current stack:", stack.items)
    print("Top value using peek():", stack.peek())

    # LIFO means Last-In, First-Out.
    # The last value added (40) is the first value removed.
    print("\nRemoving stack values using LIFO:")

    while not stack.is_empty():
        print("Popped:", stack.pop())

    print("\nAttempting to pop from an empty stack:")
    print("Result:", stack.pop())

    print("\nAttempting to peek at an empty stack:")
    print("Result:", stack.peek())

    single_stack = Stack()
    single_stack.push(99)

    print("\nTesting a stack with one item:")
    print("Popped:", single_stack.pop())
    print("Is the stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print("Added 10, 20, 30, and 40 to the queue.")
    print("Current queue:", list(queue.items))
    print("Front value:", queue.front())

    # FIFO means First-In, First-Out.
    # The first value added (10) is the first value removed.
    print("\nRemoving queue values using FIFO:")

    while not queue.is_empty():
        print("Dequeued:", queue.dequeue())

    print("\nAttempting to dequeue from an empty queue:")
    print("Result:", queue.dequeue())

    print("\nAttempting to view the front of an empty queue:")
    print("Result:", queue.front())

    single_queue = Queue()
    single_queue.enqueue(99)

    print("\nTesting a queue with one item:")
    print("Dequeued:", single_queue.dequeue())
    print("Is the queue empty?", single_queue.is_empty())

    # ===============================
    # REAL-WORLD SCENARIOS
    # ===============================

    # A stack can represent the undo history in a text editor.
    # The most recent action is the first action undone.
    print("\n=== REAL-WORLD STACK: TEXT EDITOR UNDO ===")

    undo_history = Stack()
    undo_history.push("Typed introduction")
    undo_history.push("Added second paragraph")
    undo_history.push("Changed heading")

    print("Most recent action:", undo_history.peek())
    print("Undoing:", undo_history.pop())
    print("Undoing:", undo_history.pop())

    # A queue can represent customer support requests.
    # Requests are processed in the order they arrive.
    print("\n=== REAL-WORLD QUEUE: CUSTOMER SUPPORT ===")

    support_tickets = Queue()
    support_tickets.enqueue("Ticket A")
    support_tickets.enqueue("Ticket B")
    support_tickets.enqueue("Ticket C")

    print("Next ticket:", support_tickets.front())

    while not support_tickets.is_empty():
        print("Processing:", support_tickets.dequeue())


if __name__ == "__main__":
    main()
