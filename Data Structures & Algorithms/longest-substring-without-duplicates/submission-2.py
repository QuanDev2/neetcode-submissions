"""
hashmap to keep track of visited char: char -> char idx last seen
l, r pointers
r 0 -> end
for each r:
    if r in visited, move left by 1
    else, add r to visited
    update hashmap
    update maxLen = max(maxLen, r - l + 1)

zxyzxyz
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        visited = {} # char -> idx
        for r, c in enumerate(s):
            if c in visited:
                l = max(l, visited[c] + 1)
            visited[c] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen
