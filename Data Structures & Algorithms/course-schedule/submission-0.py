class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        states = [0] * numCourses
        # state: 0 = not visited, 1 = visited (detecting cycle), 2 = visited (skip)

        def dfs(course):
            if states[course] == 1: # if see a visiting course again, then it's a cycle
                return False
            if states[course] == 2: # if already visited and not a cycle, early return
                return True

            states[course] = 1 # mark visiting
            for preq in courses[course]:
                if not dfs(preq):
                    return False
            
            states[course] = 2

            return True
        
        ##
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        
        

