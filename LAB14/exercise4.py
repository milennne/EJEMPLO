# List to store test results
test_results = []

# Function to record each test result
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"  # ✅ if passed, ❌ if failed
    test_results.append(f"{emoji} {test_name}")  # Add result to the list


class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize the heap as an empty list

    def delete_min(self):
        # ❌🆙 Remove the root (minimum element)
        if not self.heap:  # If the heap is empty, return None
            return None
        root = self.heap[0]        # Store the minimum (root)
        last = self.heap.pop()     # Remove the last element

        # If the heap still has elements, move last to root and heapify down
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root  # Return the removed minimum element

    def _heapify_down(self, index):
        # ⬇️ Move the element at index down to maintain heap property
        size = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2  # Left and right child indices
            smallest = index  # Assume current index is the smallest

            # Check if left child is smaller
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check if right child is smaller than current smallest
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If smallest is not the current index, swap and continue
            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest  # Continue from new index
            else:
                break  # Heap property is satisfied

    def _left_child_index(self, index):
        return 2 * index + 1  # Return index of left child

    def _right_child_index(self, index):
        return 2 * index + 2  # Return index of right child

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

    def size(self):
        return len(self.heap)  # Return current number of elements

def test_1_4():
    heap = MinHeap()
    
    # 1.4.1 Deleting from an empty heap
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)
    
    # 1.4.2 Deleting when there is only one element
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)
    
    # 1.4.3 Deleting multiple elements in sequence
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)
    
    # 1.4.4 Check that heap property is maintained after deletion
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] <= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)
    
    # 1.4.5 Check that the size decreases after deletion
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)
# 🚀 Execute tests
test_1_4()

# 📋 Display summary of test results
for r in test_results:
    print(r)

