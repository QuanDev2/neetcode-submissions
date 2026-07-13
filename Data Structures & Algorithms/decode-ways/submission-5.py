class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Returns the number of ways to decode string s starting from pos i
        i == n => string to decode is "" => only 1 way
        at pos i, we can decode by taking s[i] (1 char) or s[i] and s[i+1] (2 chars)
        Note: char = '0' => invalid => 0 ways to decode this
        """
        n = len(s)
        # memoi = {}
        # def decodeFrom(i: int) -> int:
        #     if i == n:
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     if i not in memoi:
        #         # start the actual consuming
        #         ways = 0
        #         # process 1 char
        #         ways += decodeFrom(i+1)
        #         # process 2 chars: 10, 11, 12...19, 20, 21...26
        #         if i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
        #             ways += decodeFrom(i+2)
        #         memoi[i] = ways
        #     return memoi[i]
            
        # return decodeFrom(0)

        ### Tabulation
        tab = [0] * (n+1)
        tab[-1] = 1
        # 1 2 3 ''
        # 0 0 0 1  # tab holds the ways of decoding string from pos i onward
        for i in reversed(range(n)):
            if s[i] == '0':
                continue
            # add ways of single char
            tab[i] = tab[i+1]
            if i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                tab[i] += tab[i+2]
        return tab[0]

