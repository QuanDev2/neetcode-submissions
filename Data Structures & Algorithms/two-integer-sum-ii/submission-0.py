class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # list is sorted, use 2 idxs, move either one depending on sum vs target
        start, end = 0, len(numbers)-1
        while start < end:
            c_sum = numbers[start] + numbers[end]
            if c_sum == target:
                return [start+1, end+1]
            if c_sum < target:
                start += 1
            else:
                end -= 1
        
        return []
