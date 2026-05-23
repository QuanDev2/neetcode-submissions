class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = self.getDictFromString(s)
        t_dict = self.getDictFromString(t)
        for k, v in s_dict.items():
            if k not in t_dict:
                return False
            if v != t_dict[k]:
                return False
        return True
            
    
    def getDictFromString(self, s: str) -> dict:
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        return s_dict