class TimeMap:
    """
    hashmap key -> [(timestamp, value)]
    retrieve val, then binary search
    """

    def __init__(self):
        self.hashmap = defaultdict(list)
               
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))      

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        vals = self.hashmap[key]
        i, j = 0, len(vals)-1
        while i <= j:
            mid = (i+j)//2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif timestamp < vals[mid][0]:
                j = mid - 1
            else:
                i = mid + 1

        return vals[j][1] if j >= 0 else ""

