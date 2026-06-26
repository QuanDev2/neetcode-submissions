class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        iterate the matrix, sees 1 -> found the start of a new island -> increment island counter
        when found an island, dfs in 4 directions, flip 1 to 0 to avoid duplicate traversal on future iteration
        """
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return

            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dR, dC in deltas:
                dfs(r + dR, c + dC)

        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt+=1
                    dfs(r, c)
        
        return cnt
