
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        pop = 0
        for _ in range(k):
            pop = heapq.heappop(maxHeap)
        return -pop