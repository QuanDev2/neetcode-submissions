"""
Time: O(n)
space: O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # aba 
        # !abba 
        # abca
        # 2 pointers from either end
        h, t = 0, len(s)-1
        while h < t:
            while h < t and not s[h].isalnum():
                h += 1  

            while h < t and not s[t].isalnum():
                t -= 1  

            if s[h].lower() != s[t].lower():
                return False
            h += 1
            t -= 1
        return True