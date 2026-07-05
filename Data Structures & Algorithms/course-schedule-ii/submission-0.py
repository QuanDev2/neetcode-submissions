class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        states = [0] * numCourses
        # states: 0 = not visited, 1 = visiting, 2 = visited
        prereqs = defaultdict(list)
        for c, p in prerequisites:
            prereqs[c].append(p)
        
        def detectCycle(c):
            if states[c] == 1:
                return True
            if states[c] == 2:
                return False
            states[c] = 1
            for p in prereqs[c]:
                if detectCycle(p):
                    return False
            states[c] = 2
            res.append(c)
            return False

        res = []
        for c in range(numCourses):
            if detectCycle(c):
                return []
        return res