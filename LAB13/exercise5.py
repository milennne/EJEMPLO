class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):

        while i != 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _heapify_down(self, i):

        while True:
            left_child = (2 * i) + 1
            right_child = (2 * i) + 2
            maximum = i

            if left_child < len(self.heap) and self.heap[maximum] < self.heap[left_child]:
                maximum = left_child
            if right_child < len(self.heap) and self.heap[maximum] < self.heap[right_child]:
                maximum = right_child

            if maximum == i:
                break

            self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i]
            i = maximum

    def delete_max(self):
        if not self.heap:
            return 
        val_deleted = self.heap[0]

        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)

        return val_deleted
    
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print("🦁 Test 1:", h.heap==[1])
    for v in [3,2,8,5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0]==max(h.heap))
    h.delete_max();      print("🦁 Test 3:", h.heap[0]==max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print("🦁 Test 4:", h.heap==[3,1])
    h=MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max()==10 and h.heap==[])

test_max_heap()
