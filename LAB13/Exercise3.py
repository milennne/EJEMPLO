class MinHeap:
    """📦 MinHeap data structure using list."""

    def __init__(self):
        # Initialize empty list for heap
        self.heap = []

    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0


class MinHeap(MinHeap):
    def delete_min(self):
        # ❌🆙 Remove root
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        # ⬇️ Swap with smaller child
        size = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break


# 🧪 Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    
    h.heap = [1]
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    
    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    
    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    
    h.heap = [1, 2, 3, 4, 5]
    print("🧹 Test 5:", h.delete_min() == 1 and h.heap == [2, 4, 3, 5])


# ▶️ Run the test function
test_min_heap_delete_min()
