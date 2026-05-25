class Solution:
    def encode(self, strs: List[str]) -> str:
        # use "length#string"
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s

        return res
        
    def decode(self, s: str) -> List[str]:
        # s = "3#cab2#hi"
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            i = j + 1 # i = 2
            j = i + s_len # j = 5
            res.append(s[i:j])
            i = j
        
        return res
