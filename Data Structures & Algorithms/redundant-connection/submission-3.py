class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1)) # index 0 is unused
        rank = [1] * (n+1)

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        # return true when same partition, false otherwise
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX == rootY:
                return False # same partition, there's nothing to do

            if rank[x] < rank[y]:
                rootX, rootY = rootY, rootX
            
            parent[rootY] = rootX
            rank[x] += rank[y]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
            

