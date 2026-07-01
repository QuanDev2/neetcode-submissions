class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        visited = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

        q = deque()
        # get all outer pacific islands
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    q.append((r, c))
                    visited.add((r, c))
                    pacific.add((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    pacific.add((nr, nc))

        
        # process atlantic
        visited.clear()
        q.clear()
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS-1 or c == COLS-1:
                    q.append((r, c))
                    visited.add((r, c))
                    atlantic.add((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    atlantic.add((nr, nc))

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

        

