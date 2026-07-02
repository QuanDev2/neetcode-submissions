class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get all border cells to start
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS-1 or c == COLS-1) and board[r][c] == 'O':
                    q.append((r, c))
                    board[r][c] = 'E'
        print('board 1')
        print(board)

        
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                    board[nr][nc] = 'E'
                    q.append((nr, nc))
        print(board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'