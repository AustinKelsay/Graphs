class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
        
def earliest_ancestor(ancestors, starting_node):
    # Create an empty queue and enqueue the starting path
    queue = Queue()
    path = [starting_node]
    queue.enqueue(path)
    # Create an empty set to track visited parents (first of the pair)
    visited = set()
    # While the queue is not empty:
    while queue.size() > 0:
        # get current pair (dequeue from queue)
        current_pair = queue.dequeue()
        neighbor = []
        # iterate through your current pair:
        for i in current_pair:
            for pairs in ancestors:
                if pairs[1] == i and i not in visited:
                    visited.add(i)
                    neighbor.append(pairs[0])
                    queue.enqueue(neighbor)
        
        if len(neighbor) <= 0:
            if current_pair[0] == starting_node:
                return -1
            else:
                return current_pair[0]