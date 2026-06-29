class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                row, col = queue.popleft()
                for dR, dC in deltas:
                    nR, nC = row + dR, col + dC
                    if nR < 0 or nR >= len(grid) or nC < 0 or nC >= len(grid[0]) or grid[nR][nC] == '0':
                        continue
                    grid[nR][nC] = '0'
                    queue.append((nR, nC))

        
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt += 1
                    bfs(r, c)
        return cnt

