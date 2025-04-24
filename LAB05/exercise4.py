class Deque:
    """Double-ended queue implementation for sliding window."""

    def __init__(self):
        """Initialize an empty deque."""
        self.items = []

    def is_empty(self):
        """Check if deque is empty."""
        return len(self.items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the front item from the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop(0)

    def remove_rear(self):
        """Remove and return the rear item from the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop()

    def peek_front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[0]

    def peek_rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[-1]

    def size(self):
        """Return the number of items in the deque."""
        return len(self.items)


def sliding_window_maximum(nums, k):
    """Find maximum elements in sliding windows of size k."""
    if not nums or k <= 0:
        return []

    # Edge cases: k = 1 or k > length of array
    if k == 1:
        return nums
    if k > len(nums):
        return [max(nums)]

    result = []  # To store maximum values 📊
    deque = Deque()  # Using our Deque implementation

    # Process the first k elements (first window) 🔎
    for i in range(k):
        # Remove smaller elements from the back
        # (they won't be maximum in current window) 🧹
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        # Add current index to the deque
        deque.add_rear(i)

    # Process the rest of the elements
    for i in range(k, len(nums)):
        # The front of deque contains the maximum for previous window
        result.append(nums[deque.peek_front()])

        # Remove elements outside the current window 🪟
        while not deque.is_empty() and deque.peek_front() <= i - k:
            deque.remove_front()

        # Remove smaller elements from the back
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        # Add current index to the deque
        deque.add_rear(i)

    # Add the maximum for the last window
    result.append(nums[deque.peek_front()])

    return result


def test_sliding_window_maximum():
    """Test sliding window maximum algorithm."""
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 5, 6, 7, 8]),
        ([8, 7, 6, 5, 4, 3, 2, 1], 3, [8, 7, 6, 5, 4, 3]),
        ([1, 1, 1, 1, 1], 2, [1, 1, 1, 1])
    ]

    print("Testing sliding window maximum algorithm 🪟")
    for nums, k, expected in test_cases:
        result = sliding_window_maximum(nums, k)
        print(f"Array: {nums}")
        print(f"Window size: {k}")
        print(f"Maximum values: {result}")
        print(f"Expected: {expected}")
        print(
            f"Correct: {result == expected} {'✅' if result == expected else '❌'}\n")
        
test_sliding_window_maximum()
