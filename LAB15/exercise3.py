test_results = []

def record_test(test_name, condition):
    result = "PASSED" if condition else "FAILED"
    test_results.append(f"{result} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Automatically create vertices if they don't exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add the connection if it's not already present
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)
    
    def has_edge(self, vertex1, vertex2):
        return vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def has_vertex(self, vertex):
        return vertex in self.adjacency_list

def test_1_3():
    graph = Graph()
    
    # 1.3.1 Basic edge creation
    graph.add_vertex("Lima")
    graph.add_vertex("Cusco")
    graph.add_edge("Lima", "Cusco")
    record_test("1.3.1 Basic edge creation", graph.has_edge("Lima", "Cusco"))
    
    # 1.3.2 Bidirectional connection
    record_test("1.3.2 Bidirectional connection", graph.has_edge("Cusco", "Lima"))
    
    # 1.3.3 Auto vertex creation
    graph.add_edge("Arequipa", "Trujillo")  # Both vertices should be created automatically
    has_both = graph.has_vertex("Arequipa") and graph.has_vertex("Trujillo")
    record_test("1.3.3 Auto vertex creation", has_both)
    
    # 1.3.4 Duplicate edge prevention
    initial_neighbors = len(graph.get_neighbors("Lima"))
    graph.add_edge("Lima", "Cusco")  # Adding the same edge again
    final_neighbors = len(graph.get_neighbors("Lima"))
    record_test("1.3.4 Duplicate edge prevention", initial_neighbors == final_neighbors)
    
    # 1.3.5 Connection verification
    lima_neighbors = graph.get_neighbors("Lima")
    record_test("1.3.5 Connection verification", "Cusco" in lima_neighbors)

# Run tests
test_1_3()

# Summary
for result in test_results:
    print(result)
