
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        stack = [node]
        seen = set()
        
        # maps nodes to neighbors (using vals)
        neighbor_dict = {}
        
        # maps vals to clones with said val
        clone_dict = {}
        
        while (len(stack)):
            current = stack.pop()
            seen.add(current)
            
            neighbor_dict[current.val] = list(map(lambda neighbor : neighbor.val, current.neighbors))
            
            for neighbor in current.neighbors:
                if neighbor not in seen:
                    stack.append(neighbor)
        
        for n in range(1, len(neighbor_dict) + 1):
            clone = Node(n)
            clone_dict[n] = clone
        
        for n in range(1, len(clone_dict) + 1):
            clone = clone_dict[n]
            clone.neighbors = list(map(lambda val : clone_dict[val], neighbor_dict[clone.val]))
        
        return clone_dict[1]
    
class Main:
    sol = Solution()
    
    print(sol.cloneGraph(Node(1, [Node(2)])).neighbors)