"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        # take original node, returns cloned node
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node) if node else None