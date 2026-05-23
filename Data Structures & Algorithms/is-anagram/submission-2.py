# O(n) time from building the dict; O(1) space

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = self.getDictFromString(s)
        t_dict = self.getDictFromString(t)
        return s_dict == t_dict
        # can also sort the strings, returning sorted(s) == sorted(t)
            
    
    def getDictFromString(self, s: str) -> dict:
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        return s_dict