class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [-1,0,1,2,-1,-4]
        s_nums = [-4, -1, -1, 0, 1, 2]
        sorted, then iterate, check if 2 of remaining numbers add up to 1 with 2 pointes

        ** Handle dups in 3 places: outer loop, and inner loop after found
        """
        s_nums = sorted(nums)
        res = []
        for i, n in enumerate(s_nums):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue

            s = i + 1 # start
            e = len(nums) - 1 # end
            target = -n
            while (s < e):
                if s_nums[s] + s_nums[e] == target:
                    res.append([n, s_nums[s], s_nums[e]])
                    s += 1
                    e -= 1

                    while s < e and s_nums[s] == s_nums[s-1]:
                        s += 1

                    while s < e and s_nums[e] == s_nums[e+1]:
                        e -= 1

                elif s_nums[s] + s_nums[e] < target:
                    s += 1
                else:
                    e -= 1

        return res



