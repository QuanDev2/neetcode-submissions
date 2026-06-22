class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stop when len <= 1
        # max heap. pop 2, smash, push back
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)
            diff = abs(s1 - s2)

            if diff != 0:
                heapq.heappush(maxHeap, -diff)

        if not maxHeap:
            return 0

        return -maxHeap[0]