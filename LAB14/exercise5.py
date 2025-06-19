test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []
    
    def insert(self, value):
        # Add the new value at the end of the list
        self.heap.append(value)
        # Restore the max-heap property by bubbling up
        self._heapify_up(len(self.heap) - 1)
    
    def delete_max(self):
        # Remove and return the maximum element (the root)
        if not self.heap:
            return None
        data_del = self.heap[0]  # Store the max value to return later
        last_item = self.heap.pop(0)  # Remove the first element (root)
        if self.heap:
            self.heap[0] = last_item  # Replace root with last item
            self._heapify_down(last_item)  # Restore heap property
        return data_del

    def build_heap(self, array):
        # Construct a heap from an unordered array
        self.heap = []
        for val in array:
            self.insert(val)  # Insert each element and heapify up
    
    def _heapify_up(self, index):
        # Move the element at index up until the heap property is restored
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                # Swap if child is greater than parent (max-heap property)
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                continue
            break

    def _heapify_down(self, index):
        # Move the element at index down until the heap property is restored
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            maximum = index

            # Compare with left and right children
            if left_child < len(self.heap) and self.heap[maximum] < self.heap[left_child]:
                maximum = left_child
            if right_child < len(self.heap) and self.heap[maximum] < self.heap[right_child]:
                maximum = right_child
            
            if index == maximum:
                break  # Heap property is satisfied
            
            # Swap with the larger child and continue down
            self.heap[maximum], self.heap[index] = self.heap[index], self.heap[maximum]
            index = maximum


def test_1_5():
    heap = MaxHeap()
    
    # 1.5.1 MaxHeap insertion
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)
    
    # 1.5.2 MaxHeap deletion
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)
    
    # 1.5.3 Build heap from array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))
    
    # 1.5.4 Heap property verification
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)
    
    # 1.5.5 Empty array handling
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# 🚀 Run tests
test_1_5()

# 📋 Summary
for r in test_results:
    print(r)

    