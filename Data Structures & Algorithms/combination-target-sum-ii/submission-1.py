class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(path: List[int], choices: List[int], sum: int) -> None:
            if sum == target:
                res.append(path.copy())
                return
            for i, choice in enumerate(choices):
                if sum + choice > target:
                    return
                if i > 0 and choice == choices[i-1]:
                    continue
                
                path.append(choice)
                backtrack(path, choices[i+1:], sum + choice)
                path.pop()

        backtrack([], sorted(candidates), 0)
        return res