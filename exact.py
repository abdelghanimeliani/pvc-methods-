from graph import Base_Graph, Node
from typing import List, Tuple
from itertools import permutations

class Exact_TSP_Graph(Base_Graph):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def exact_solution(self, origin: Node) -> Tuple[List[Node], float]:
        """
        Return the exact solution of the problem as a path, cost tuple
        """
        path = [origin]
        cost = float('inf')
        nodes = [node for node in self.nodes if node != origin]
        for permutation in permutations(nodes):
            weight = 0
            current = origin
            for node in permutation:
                weight += self.get_distance(current, node)
                current = node
            weight += self.get_distance(current, origin)
            if weight < cost:
                cost = weight
                path += list(permutation) + [origin]
        return path, cost


g = Exact_TSP_Graph(
    nodes = [Node(label) for label in ['A', 'B', 'C', 'D']],
    edges = {
        ('A', 'B'): 1,
        ('A', 'C'): 2,
        ('A', 'D'): 3,
        ('B', 'C'): 4,
        ('B', 'D'): 5,
        ('C', 'D'): 6
    }
)

print(g.exact_solution('A'))