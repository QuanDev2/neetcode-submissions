class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0
        visited = set()
        
        def dfs(node: int, parent: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
        
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, -1)
        return res