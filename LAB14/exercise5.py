test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        # Add value maintaining max-heap property
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete_max(self):
        # Remove and return maximum element
        if not self.heap:
            return None
        data_del = self.heap[0]
        last_item = self.heap.pop(0)
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(last_item)
        return data_del

    
    def build_heap(self, array):
      # Convert array to valid heap in O(n) time
        self.heap = []
        for val in array:
            self.insert(val)
    
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                continue
            break 

    
    def _heapify_down(self, index):
        # Move element down for max-heap        
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            maximum = index

            if left_child < len(self.heap) and self.heap[maximum] < self.heap[left_child]:
                maximum = left_child
            if right_child < len(self.heap) and self.heap[maximum] < self.heap[right_child]:
                maximum = right_child
            if index == maximum:
                break
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

    