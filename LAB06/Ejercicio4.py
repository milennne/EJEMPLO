class CircularQueue:
    """Queue implementation using a circular array."""

    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Queue is full! 💥")

        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"

class Process:
    """Represent a process in a task scheduler."""

    def __init__(self, id, burst_time):
        """Initialize a process with ID and CPU burst time."""
        self.id = id
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def __str__(self):
        """Return a string representation of the process."""
        return f"Process #{self.id} (Remaining: {self.remaining_time})"


def round_robin_scheduler(processes, time_quantum):
    """Simulate round-robin scheduling using a circular queue."""
    if not processes or time_quantum <= 0:
        return []

    # Create a circular queue for processes
    n = len(processes)
    queue = CircularQueue(n)

    # Add all processes to the queue
    for process in processes:
        queue.enqueue(process)

    current_time = 0
    completion_times = {}

    print("Starting Round Robin scheduling simulation... ⏱️")

    # Process until queue is empty
    while not queue.is_empty():
        # Get the next process
        process = queue.dequeue()

        # Determine execution time for this quantum
        execution_time = min(time_quantum, process.remaining_time)

        # Update current time and process remaining time
        current_time += execution_time
        process.remaining_time -= execution_time

        print(f"Executed {process} for {execution_time} time units ⚙️")

        # If process is not complete, add it back to queue
        if process.remaining_time > 0:
            queue.enqueue(process)
        else:
            # Process is complete
            completion_times[process.id] = current_time
            print(f"Process #{process.id} completed at time {current_time} ✅")

    return completion_times




def test_round_robin_scheduler():
    """Test round-robin scheduler using circular queue."""
    #Case1
    processes = [
        Process(1, 10),
        Process(2, 5),
        Process(3, 8)
    ]
    time_quantum = 2
    completion_times = round_robin_scheduler(processes, time_quantum)
    expected = {1: 23, 2: 15, 3: 21}
    for process_id, time in expected.items():
        assert completion_times[process_id] == time, f"Process {process_id} should complete at time {time}"
    print("✅ Test 1: Round-robin scheduler test passed!")

    #Case2
    processes2 = [
        Process(1, 4),
        Process(2, 4),
        Process(3, 4),
        Process(4, 4)
    ]
    time_quantum2 = 2
    completion_times2 = round_robin_scheduler(processes2, time_quantum2)
    expected2 = {1: 10, 2: 12, 3: 14, 4: 16}
    for process_id, time in expected2.items():
        assert completion_times2[process_id] == time, f"Process {process_id} should complete at time {time}"
    print("✅ Test 2: All equal burst times test passed!")

    #Case3
    processes3 = [
        Process(1, 3),
        Process(2, 7),
        Process(3, 2)
    ]
    time_quantum3 = 5
    completion_times3 = round_robin_scheduler(processes3, time_quantum3)
    expected3 = {1: 3, 2: 12, 3: 10}
    for process_id, time in expected3.items():
        assert completion_times3[process_id] == time, f"Process {process_id} should complete at time {time}"
    print("✅ Test 3: Large quantum test passed!")

    return True

if __name__ == "__main__":
    test_round_robin_scheduler()