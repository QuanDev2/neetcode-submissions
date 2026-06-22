
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        # maxHeap = [-x for x in nums]
        # heapq.heapify(maxHeap)
        # pop = 0
        # for _ in range(k):
        #     pop = heapq.heappop(maxHeap) O(logn)
        # return -pop

        # O(klogn) => not efficient. use min heap of size k
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, num)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return maxHeap[0]
        
