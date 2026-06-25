class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def isPalin(s, l, r):
        #     while l < r:
        #         if s[l] != s[r]: return False
        #         l += 1; r -= 1
        #     return True

        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
            
            print(start)
            print(s)
            print(len(s))
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    path.append(s[start:i+1])
                    dfs(i+1, path)
                    path.pop()

        res = []
        dfs(0, [])
        return res
