class Solution:
    def longestPalindrome(self, s: str) -> str:
        def detectPalindrome(l: int, r: int) -> tuple:
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)
        
        best = ''
        for i in range(len(s)):
            l, r = detectPalindrome(i, i)
            oddS = s[l:r+1]
            l, r = detectPalindrome(i, i+1)
            evenS = s[l:r+1]
            longer = oddS if len(oddS) > len(evenS) else evenS
            if len(longer) > len(best):
                best = longer
        return best