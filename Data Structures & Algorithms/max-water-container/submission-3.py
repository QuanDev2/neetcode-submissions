class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # max_water = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         print((j-i) * min(heights[j], heights[i]))
        #         max_water = max(max_water, (j-i) * min(heights[j], heights[i]))
        # return max_water

        # move the smaller height
        max_water = 0
        i, j = 0, len(heights) - 1
        while i < j:
            max_water = max(max_water, (j-i) * min(heights[j], heights[i]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_water
