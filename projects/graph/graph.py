"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            # Creae the new key with the vertex id and set the value with an empty set
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if v1 and v2 are actually vertices in our graph
        if v1 in self.vertices and v2 in self.vertices:
            # Get v1 from our vertices, add v2 to the set of edges
            self.vertices[v1].add(v2)

    # Extracurriculur method that adds an edge that goes in both directions
    def add_bidirected_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    # Breadth first traversal = focus on diversification/propogation over a specific destination
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty queue and enqueue the starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited vertices
        visited = set()
        # While the que is not empty:
        while queue.size() > 0:
            # get current vertex (dequeue from queue)
            current_vertex = queue.dequeue()
            # check if the current vertex has not been visited:
            if current_vertex not in visited:
                # print the current vertex
                print(current_vertex)
                # Mark the current vertex as visited
                visited.add(current_vertex)
                # queue up all of the vertex's neighbors (so we can visit them next)
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    # Depth first traversal  
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty STACK and push the PATH TO starting vertex (so just the starting vertex)
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to track visited vertices
        visited = set()

        # While the que is not empty:
        while stack.size() > 0:
            # get current PATH (dequeue from queue)
            current_path = stack.pop()
            # set the current PATH to the LAST element in the PATH

            # check if the current path has not been visited:
            if current_path not in visited:
                # add to visited
                visited.add(current_path)
                print(current_path)

                for next_vertex in self.get_neighbors(current_path):
                    stack.push(next_vertex)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        visited = set()
        def inner_dft(current):
            if current == None:
                return
            else:
                if current not in visited:
                    print(current)
                    visited.add(current)
                    for next_v in self.get_neighbors(current):
                        s.push(next_v)
                    inner_dft(s.pop())
                else:
                    inner_dft(s.pop())
        inner_dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the starting vertex
        queue = Queue()
        visited_vertices = set()
        # Create an empty set to track visited vertices
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # While the que is not empty:
        while queue.size() > 0:
            # get current vertex (dequeue from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # Mark the current vertex as visited
                visited_vertices.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path

                # queue up NEW paths with each neighbor
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(vertex)
                    queue.enqueue({
                        'current_vertex': vertex,
                        'path': new_path
                    })


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited_vertices = set()
        # Create an empty set to track visited vertices
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # While the que is not empty:
        while stack.size() > 0:
            # get current vertex (dequeue from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # Mark the current vertex as visited
                visited_vertices.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path

                # queue up NEW paths with each neighbor
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(vertex)
                    stack.push({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        def dft_inner(current_path):
            current_vertex = current_path.pop()
            current_path.append(current_vertex)
            if current_vertex == destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor in self.get_neighbors(current_vertex):
                        path_to_add = current_path + [neighbor]
                        stack.push(path_to_add)
                    return dft_inner(stack.pop())
                else:
                    return dft_inner(stack.pop())

        return dft_inner([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
