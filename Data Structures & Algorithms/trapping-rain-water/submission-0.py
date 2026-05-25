class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, minLR, water = [0]*len(height), [0]*len(height), [0]*len(height), [0]*len(height)
        for i in range(len(height)):
            if i == 0:
                continue
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for j in reversed(range(len(height))):
            if j == len(height) - 1:
                continue
            maxRight[j] = max(maxRight[j+1], height[j+1])
        water_count = 0
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                water_count += water
        return water_count
        