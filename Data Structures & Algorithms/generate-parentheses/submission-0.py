class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path: List[int], open: int, close: int):
            if open == n and close == n:
                res.append("".join(path.copy()))
                return

            if open < n:
                path.append('(')
                dfs(path, open+1, close)
                path.pop()
            if close < open:
                path.append(')')
                dfs(path, open, close+1)
                path.pop()

        res = []
        dfs([], 0, 0)
        print(res)
        return res