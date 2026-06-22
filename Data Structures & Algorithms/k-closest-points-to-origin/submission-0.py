class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(-(x*x + y*y), x, y) for (x, y) in points]
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        return [[x, y] for (_, x, y) in maxHeap ]