"""
Input: [3, 5, 6, 2].
We need left boundary L, right boundary R, and height H to calculate the area.
for any given bar, its L is the shorter and closest to it.
R = height of the next bar that's shorter than it.
H = its height.
Stack to store the bars that could be the L for a future bar.
If bar[i] is taller than top of stack => it knows that it could be a part of an even wider rectangle.
Else, bar[i] knows that its the R of the rectangle that top of stack belongs to.
So when we see bar[i] with height < top of stack height => pop top of stack and calculate the rectangle it could belong to, starting by itself.
Then keep popping the stack to expand the rectangle until stack is empty.

For increasing input: [1, 3, 6]
stack won't be processed in main iteration.
Then we have to set R = len, and keep popping the stack to calculate the area.

formular: area = (R - L - 1) * height of top of stack

Time: O(n)
Space: O(n)
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