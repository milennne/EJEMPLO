test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add the edge in both directions for undirected graph
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def get_degree(self, vertex):
        # Return the number of connections (neighbors) for the vertex
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])
        return 0  # Return 0 if the vertex does not exist

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        # DFS-based helper function to find all paths
        def dfs(current, end, path, paths):
            if max_length is not None and len(path) > max_length:
                return
            if current == end:
                paths.append(path[:])
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, end, path, paths)
                    path.pop()

        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []  # One or both vertices do not exist

        all_paths = []
        dfs(start_vertex, end_vertex, [start_vertex], all_paths)
        return all_paths

    def get_connected_components(self):
        visited = set()
        components = []

        # DFS to collect connected nodes
        def dfs(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)

        return components


def test_1_5():
    graph = Graph()

    # Create a graph with 2 components
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Separate component

    # 1.5.1 Degree calculation
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)

    # 1.5.2 Multiple paths finding
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)

    # 1.5.3 Connected components
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)

    # 1.5.4 Empty graph analysis
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])

    # 1.5.5 Non-existent vertex handling
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0 or degree is None)

# Run tests
test_1_5()

# Summary
for r in test_results:
    print(r)
