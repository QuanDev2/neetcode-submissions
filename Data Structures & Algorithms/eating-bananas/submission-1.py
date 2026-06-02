class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            timeToEat = sum(math.ceil(p / mid) for p in piles)
            if timeToEat <= h:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo