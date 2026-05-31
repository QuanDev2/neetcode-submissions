"""
Input: [3, 5, 6, 2].
the stack stores the bars that could potentially be the left boundary of a future bar. Stack should have increasing order, bottom to top (top is tallest).
So at bar i, if bar i taller than top of stack (T), then top of stack knows that it can be a part of a wider rectangle that includes bar i, so we push bar i to top of stack.

For any element in the stack, its left boundary is the one below it. That's why we always know L. We just need to find R by checking if heights[i] < T

formular: area = (R - L - 1) * height of top of stack
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
                continue
            while stack and stack[-1][1] >= h:
                top = stack.pop()
                L = stack[-1][0] if stack else -1
                maxArea = max(maxArea, (i - L - 1) * top[1])
            stack.append((i, h))

        while stack:
            top = stack.pop()
            R = len(heights)
            L = stack[-1][0] if stack else -1
            maxArea = max(maxArea, (R - L - 1) * top[1])
        
        return maxArea