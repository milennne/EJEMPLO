test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        
    
    def _heapify_up(self, index):
        # Move element up to restore min-heap property
        while index > 0:
          parent = (index - 1) // 2
          if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            continue
          break

    
    def _parent_index(self, index):
        return (index - 1) // 2 if index > 0 else -1
    
    def size(self):
        return len(self.heap)
    
    def peek(self):
        return self.heap[0] if self.heap else None

def test_1_3():
    heap = MinHeap()
    
    # 1.3.1 Single element insertion
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])
    
    # 1.3.2 Multiple insertions
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)
    
    # 1.3.3 Minimum tracking
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)
    
    # 1.3.4 Heap property validation
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)
    
    # 1.3.5 Size consistency
    record_test("1.3.5 Size consistency", heap.size() == 4)

# 🚀 Run tests
test_1_3()

# 📋 Summary
for r in test_results:
    print(r)
