class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_cnt = 0
        moves = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            print(q)
            print(grid)
            for i in range(len(q)):
                r, c = q.popleft()
                # if grid[r][c] == 1:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh_cnt -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            if q: 
                moves += 1
            print(moves)
          
            

        return moves if fresh_cnt == 0 else -1

        """
Time: O(n*m) = Space
        """

