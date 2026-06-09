"""
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = defaultdict(int)
        maxFreq = 0
        maxLen = 0
        for r, c in enumerate(s):
            windowSize = r - l + 1
            freqs[c] += 1
            maxFreq = max(maxFreq, freqs[c])
            minChange = windowSize - maxFreq
            if minChange > k:
                # shifting left up by one, decrement freq
                freqs[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen

