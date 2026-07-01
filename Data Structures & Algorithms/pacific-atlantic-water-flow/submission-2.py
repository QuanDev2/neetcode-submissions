class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(starts: set, ocean: set) -> None:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
            q = deque(starts)
            ocean |= starts
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
                        ocean.add((nr, nc))

        
        pacificStart = set()
        atlanticStart = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        # get all outer islands
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacificStart.add((r, c))
                if r == ROWS-1 or c == COLS-1:
                    atlanticStart.add((r, c))

        bfs(pacificStart, pacific)
        bfs(atlanticStart, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

        

