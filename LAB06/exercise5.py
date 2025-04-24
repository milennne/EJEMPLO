class CircularBuffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size_count = 0
        self.items = [None] * capacity 

    def is_empty(self):
        return self.size_count == 0

    def is_full(self):
        return self.size_count == self.capacity

    def add(self, item):

        if self.is_full():
            self.items[self.front] = item
            self.front = (self.front + 1) % self.capacity
            self.rear = (self.rear + 1) % self.capacity
        else:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size_count += 1

    def get_latest(self):

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(self.items[index])
            index = (index + 1) % self.capacity
        return result

    def get_stats(self):

        data = self.get_latest()
        if not data:
            return {"avg": None, "min": None, "max": None}
        
        try:
            avg = sum(data) / len(data)
            return {
                "avg": avg,
                "min": min(data),
                "max": max(data)
            }
        except TypeError:
            return "Error: The data are not numerical"

    def display(self):
        if self.is_empty():
            return "Buffer = []"
        result = []
        index = self.front
        for i in range(self.size_count):
            result.append((self.items[index]))
            index = (index + 1) % self.capacity
        return f"Buffer: {result}"
    

def test_circular_buffer():
    print("== Test 1: Add less than capacity ==")
    cb = CircularBuffer(5)
    cb.add(1)
    cb.add(2)
    cb.add(3)
    print(cb.display())  # Buffer: [1, 2, 3]
    print("Stats:", cb.get_stats())  # {'avg': 2.0, 'min': 1, 'max': 3}
    print()

    print("== Test 2: Fill to capacity ==")
    cb.add(4)
    cb.add(5)
    print(cb.display())  # Buffer: [1, 2, 3, 4, 5]
    print("Stats:", cb.get_stats())  # {'avg': 3.0, 'min': 1, 'max': 5}
    print()

    print("== Test 3: Overwrite oldest elements ==")
    cb.add(6)  # Replaces 1
    cb.add(7)  # Replaces 2
    print(cb.display())  # Buffer: [3, 4, 5, 6, 7]
    print("Stats:", cb.get_stats())  # {'avg': 5.0, 'min': 3, 'max': 7}
    print()

    print("== Test 4: Check with empty buffer ==")
    empty_cb = CircularBuffer(3)
    print(empty_cb.display())  # Buffer = []
    print("Stats:", empty_cb.get_stats())  # {'avg': None, 'min': None, 'max': None}
    print()

    print("== Test 5: Non-numeric data ==")
    mixed_cb = CircularBuffer(3)
    mixed_cb.add("a")
    mixed_cb.add("b")
    mixed_cb.add("c")
    print(mixed_cb.display())  # Buffer: ['a', 'b', 'c']
    print("Stats:", mixed_cb.get_stats())  # Error: The data are not numerical

test_circular_buffer()

