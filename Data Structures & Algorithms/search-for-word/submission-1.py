class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True
            
       
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            found = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
    
        return False


"""

Time: O(m × 4^n)

m = total cells in the board. The outer loop tries every cell as a potential starting point.
n = len(word). From each starting cell, dfs(r, c, i) recurses until i == len(word), so the tree is at most n levels deep.
At each level you branch into 4 directions, giving 1 + 4 + 16 + ... + 4^n nodes per tree, which is O(4^n).
Multiply: m starting cells × O(4^n) per tree = O(m × 4^n).

In practice it's much faster because the board[r][c] != word[i] check prunes most branches immediately. But worst case is the full tree.

Space: O(n)
No visited set, no path list. The only memory used is the call stack. The recursion goes at most n levels deep (one frame per character in word), so stack depth is O(n).
The in-place '#' trick is what keeps space O(n) instead of O(m) — you avoid allocating a separate visited structure.
"""

