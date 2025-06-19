test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        #Crea una lista vacia, los resultados de cada test 
        self.heap = []
        
    def _parent_index(self, index):
        if not isinstance(index, int) or index <= 0 or index >= len(self.heap):
            return -1  # Root or invalid index
        return (index - 1) // 2

    def _left_child_index(self, index):
        # Returns the index of the left child of node at index
        if not isinstance(index, int) or index < 0:
            return -1  # Invalid index
        return 2 * index + 1

    def _right_child_index(self, index):
        # Returns the index of the right child of node at index
        if not isinstance(index, int) or index < 0:
            return -1  # Invalid index
        return 2 * index + 2

    def _has_left_child(self, index):
        # Checks if the left child exists (within heap bounds)
        left = self._left_child_index(index)
        return 0 <= left < len(self.heap)

    def _has_right_child(self, index):
        # Checks if the right child exists (within heap bounds)
        right = self._right_child_index(index)
        return 0 <= right < len(self.heap)

def test_1_2():
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Example heap array

    # 1.2.1 Parent calculation: index 4's parent should be at index 1
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)

    # 1.2.2 Children calculation: index 1 should have children at indices 3 and 4
    left_correct = heap._left_child_index(1) == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation", left_correct and right_correct)

    # 1.2.3 Root node edge case: index 0 has no parent
    record_test("1.2.3 Root node edge case", heap._parent_index(0) == -1 or heap._parent_index(0) is None)

    # 1.2.4 Boundary validation: index 1 should have both left and right children
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)

    # 1.2.5 Invalid index handling: index 6 should not have children
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

# 🚀 Run tests
test_1_2()

# 📋 Print summary of results
for r in test_results:
    print(r)
