class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tabs = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    tabs[r][c] = 1
                else:
                    tabs[r][c] = tabs[r-1][c] + tabs[r][c-1]
        

        return tabs[-1][-1]