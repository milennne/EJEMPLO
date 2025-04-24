class QueueWithTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def __str__(self):
        return f"Queue: {self.out_stack[::-1] + self.in_stack}"


def test_queue_with_two_stacks():
    queue = QueueWithTwoStacks()
    print("Created an empty queue with two stacks.")

    print(f"Is queue empty? {queue.is_empty()}")

    print("Adding elements to queue...")
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    print(f"Queue after adding elements: {queue}")

    print(f"Front element: {queue.peek()}")

    print(f"Queue size: {queue.size()}")

    print(f"Removed element: {queue.dequeue()}")
    print(f"Queue after removing element: {queue}")

    print("Removing all elements...")
    while not queue.is_empty():
        print(f"Removed: {queue.dequeue()}")

    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error handling test: {e}")
        

def run_additional_tests():
    print("\nRunning extra tests...")

    # Test 1: Enqueue and Dequeue
    q1 = QueueWithTwoStacks()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    assert q1.dequeue() == 10
    assert q1.dequeue() == 20
    print("Test 1 passed")

    # Test 2: Peek and Size
    q2 = QueueWithTwoStacks()
    q2.enqueue("A")
    q2.enqueue("B")
    assert q2.peek() == "A"
    assert q2.size() == 2
    print("Test 2 passed")

    # Test 3: Exception on empty dequeue
    q3 = QueueWithTwoStacks()
    try:
        q3.dequeue()
    except IndexError as e:
        assert str(e) == "Queue is empty!"
        print("Test 3 passed")

if __name__ == "__main__":
    test_queue_with_two_stacks()
    run_additional_tests()
