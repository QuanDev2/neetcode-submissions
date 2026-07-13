class Solution:
    def countSubstrings(self, s: str) -> int:
        def countFromCenter(l: int, r: int) -> int:
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt
        
        cnt = 0
        for i in range(len(s)):
            cnt += countFromCenter(i, i) + countFromCenter(i, i+1)

        return cnt