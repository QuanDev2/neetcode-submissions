class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adjacenty list both directions
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set()

        def validateTreeDfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not validateTreeDfs(nei, node):
                    return False
            return True

        if not validateTreeDfs(0, -1):
            return False

        return len(visited) == n