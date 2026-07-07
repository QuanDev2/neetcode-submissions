class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        rank = [1] * (N+1)
        root = [i for i in range(N+1)]

        def findRoot(x: int) -> int:
            if x != root[x]:
                root[x] = findRoot(root[x])
            
            return root[x]

        def union(x: int, y: int) -> bool:
            rootX, rootY = findRoot(x), findRoot(y)

            if rootX == rootY:
                return False
            
            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX
            
            root[rootY] = rootX
            rank[rootX] += rank[rootY]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]