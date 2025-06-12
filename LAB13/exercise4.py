class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1

        self._heapify_up(index)

    def _heapify_up(self, i):

        while i != 0:
            parent = (i - 1) // 2
            if not self.heap[i] < self.heap[parent]:
                break
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def _heapify_down(self, i):
        while True:
            left_child = (2 * i) + 1
            right_child = (2 * i) + 2
            smallest = i

            if left_child < len(self.heap) and self.heap[smallest] > self.heap[left_child]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[smallest] > self.heap[right_child]:
                smallest = right_child
            
            if smallest == i:
                break

            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest 
 
    def extract_min(self):
        if not self.heap:
            return []
        min_delete = self.heap[0]
        last_item = self.heap.pop()

        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)

        return min_delete
    

    def peek(self):
        if not self.heap:
            return []
        return self.heap[0]
    

    def delete(self, val):
        try:
            index = self.heap.index(val)
        except ValueError:
            raise ValueError(f"Value {val} not found")

        deleted_val = self.heap[index]
        if index == (len(self.heap) - 1):
            self.heap.pop()
            return deleted_val

        self.heap[index] = self.heap.pop()

        if index < len(self.heap):
            parent = (index - 1) // 2

            if index > 0 and self.heap[index] < self.heap[parent]:
                self._heapify_up(index)
            else:
                self._heapify_down(index)

            return deleted_val


    def build_heap(self, array):
        self.heap = array
        las_non_leaf = (len(self.heap) // 2) - 1
        for i in reversed(range(0, las_non_leaf + 1)):
            self._heapify_down(i)
        


    
def test_build_heap():
    h = MinHeap()
    h.build_heap([5,3,8,1,2]); print("🔨 Test 1:", h.heap[0]==1)
    h.build_heap([7,6,5,4,3,2,1]); print("🔨 Test 2:", h.heap[0]==1)
    h.build_heap([2,1]);           print("🔨 Test 3:", h.heap==[1,2])
    h.build_heap([10]);            print("🔨 Test 4:", h.heap==[10])
    h.build_heap([]);              print("🔨 Test 5:", h.heap==[])
    
test_build_heap()
