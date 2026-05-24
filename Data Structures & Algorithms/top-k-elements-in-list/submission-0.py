class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int) # hashmap of value: freq
        for n in nums:
            freqs[n] += 1

        # dict -> list; sort by v
        sortedList = sorted(freqs.items(), key=lambda x: x[1]) # [(1, 1), (2, 2), (3, 3)]
       
        res = []
        for i in range(k):
            res.append(sortedList.pop()[0])

        return res