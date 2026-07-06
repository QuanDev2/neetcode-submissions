class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adjacenty list both directions
        if len(edges) != n - 1:
            return False
        
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set([0])
        queue = deque([(0, -1)]) # queue of (node, parent)

        while queue:
            node, parent = queue.popleft()
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, node))
                visited.add(nei)
        
        return len(visited) == n
        


        # def validateTreeDfs(node, parent):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for nei in adjList[node]:
        #         if nei == parent:
        #             continue
        #         if not validateTreeDfs(nei, node):
        #             return False
        #     return True

        # if not validateTreeDfs(0, -1):
        #     return False

        # return len(visited) == n