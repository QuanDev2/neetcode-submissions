class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        states = [0] * numCourses
        # state: 0 = not visited, 1 = visiting (detecting cycle), 2 = visited (skip)

        def detectCycle(course: int):
            if states[course] == 1:
                return True
            if states[course] == 2:
                return False
            
            states[course] = 1
            for preq in courses[course]:
                if detectCycle(preq):
                    return True
            
            states[course] = 2

            return False

        for course in range(numCourses):
            if detectCycle(course):
                return False

        return True
