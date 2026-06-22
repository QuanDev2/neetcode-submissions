class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            self.popIfExceedsK()
        print(f"init heap: {self.heap}")

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        print(self.heap)
        self.popIfExceedsK()

        print(f"returning: {self.heap[0]}")
        return self.heap[0]
        
    def popIfExceedsK(self):
        if len(self.heap) > self.k:
            print(f"popping: {self.heap[0]}")
            heapq.heappop(self.heap) 
