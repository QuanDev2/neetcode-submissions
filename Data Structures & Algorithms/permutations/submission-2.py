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

"""
Time: O(n · n!)
The recursion tree has this shape:
level 0:  1 node,   n choices each
level 1:  n nodes,  n-1 choices each
level 2:  n(n-1),   n-2 choices each
...
level n:  n! leaves (the actual permutations)
At each node you also pay O(n) for choices[:i] + choices[i+1:] (building a new list). At the leaves you pay O(n) for path.copy().
Dominant cost: O(n · n!).

Space: O(n²) auxiliary, O(n · n!) total
Auxiliary (excluding output):
At any moment the call stack is n frames deep. Each frame holds a choices slice:
frame 0: choices of length n
frame 1: choices of length n-1
frame 2: choices of length n-2
...
frame n: choices of length 0
All alive simultaneously → n + (n-1) + ... + 1 = O(n²)
Plus the path list itself: O(n). So auxiliary is O(n²).
Total (including output):
Storing n! permutations × n elements each → O(n · n!)
"""