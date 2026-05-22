class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_set = set()
        for num in nums:
            if num in visited_set:
                return True
            else:
                visited_set.add(num)
        return False