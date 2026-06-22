class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stop when len <= 1
        # max heap. pop 2, smash, push back
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap) # O(n) time

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap) # O(logn)
            diff = abs(s1 - s2)

            if diff != 0:
                heapq.heappush(maxHeap, -diff) # O(logn) time
            # Do this repeatedly -> O(nlogn) time

        if not maxHeap:
            return 0

        return -maxHeap[0]

"""
Time: O(nlogn); space: O(n)
"""