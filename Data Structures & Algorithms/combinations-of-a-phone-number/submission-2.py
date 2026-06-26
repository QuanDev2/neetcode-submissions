class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(path, start):
            # terminal condition:
            if start == len(digits):
                res.append("".join(path))
                return
            
            for c in map[digits[start]]:
                path.append(c)
                dfs(path, start+1)
                path.pop()

        res = []
        if not digits:
            return res
        dfs([], 0)
        return res
        