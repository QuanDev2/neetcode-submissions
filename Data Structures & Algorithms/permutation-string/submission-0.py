class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # build freq map for 26 chars of s1
        freq1, freqW = [0] * 26, [0] * 26
        for c in s1:
            freq1[self.ordOfChar(c)] += 1

        # build freq map for 26 chars of the first substr of s2 (length = length of s1)
        for c in s2[:len(s1)]:
            freqW[self.ordOfChar(c)] += 1
        
        matchCnt = 0
        for i in range(26):
            if freq1[i] == freqW[i]:
                matchCnt += 1
        if matchCnt == 26:
            return True

        # slide the substr window, eaach slide,
        for r in range(len(s1), len(s2)):
            # update freq map, update unmatchCnt
            lC = self.ordOfChar(s2[r - len(s1)])
            rC = self.ordOfChar(s2[r])

            # agreed → still agrees: −1 then +1 = net 0
            # disagreed → still disagrees: net 0
            # agreed → disagrees: −1 only = net −1
            # disagreed → agrees: +1 only = net +1

            if freq1[lC] == freqW[lC]:
                matchCnt -= 1
            freqW[lC] -= 1
            if freq1[lC] == freqW[lC]:
                matchCnt += 1

            # add rC
            if freq1[rC] == freqW[rC]:
                matchCnt -= 1
            freqW[rC] += 1 # slide
            if freq1[rC] == freqW[rC]:
                matchCnt += 1

            if matchCnt == 26:
                return True
        return False



        # first, # check the number of unmatched count between the 2 hashmaps, return if cnt = 0

    def ordOfChar(self, c: str) -> int:
        return ord(c) - ord('a')
