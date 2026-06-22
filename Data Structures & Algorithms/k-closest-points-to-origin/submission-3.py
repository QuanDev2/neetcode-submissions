class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maxHeap = [(-(x*x + y*y), x, y) for (x, y) in points]
        # heapq.heapify(maxHeap) # O(n)

        # while len(maxHeap) > k: # Do this (len - k) times
        #     heapq.heappop(maxHeap) # O(logn)
        # # => O((n-k)logn)
        # return [[x, y] for (_, x, y) in maxHeap ]
        # this is suboptimal because we need to heapify everything first.
        # Optimal solution: push heap one by one

        maxHeap = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(maxHeap, (-dist, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
            # Size of heap is always k => O(nlogk) time
        return [[x, y] for (_, x, y) in maxHeap ] 