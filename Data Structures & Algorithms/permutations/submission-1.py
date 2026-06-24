class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # final path has to be same length => terminal condition is length or no more choices

        res = []
        def dfs(path: List[int], choices: List[int]):
            print("+")
            print(path)
            print(choices)
            # Terminal condition
            if not choices:
                res.append(path.copy())
                return
            
            for i, num in enumerate(choices):
                path.append(num)
                dfs(path, choices[:i] + choices[i+1:])
                path.pop()

        dfs([], nums)

        return res

