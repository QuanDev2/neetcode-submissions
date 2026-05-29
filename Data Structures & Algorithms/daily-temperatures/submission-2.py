class Solution:
    """
    Mental model:
    at any given element in array, the result at that element depends on the future elements.
    Meaning, at any given elem, it can resolve all of its pass elements.
    => need a DS to keep track of all the past elements.
    Should resolve most recent element first => stack
    this stack is a waiting list of unresolved days.

    Time: O(n)
    Space: O(n)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res