"""
    ETAs can tell if car can catch up with the one in front of it.
    A car's ability to catch up and form a fleet depends on the one in front of it.
    So a car can answer the question for the one right behind it. => process from right to left (closest to destination first)
    => stack but sortet desc by pos first
    catch up when behind eta <= front eta
    O(n) time, O(n) space
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        etaPos = []
        for i in range(len(position)):
            etaPos.append(((target-position[i]) / speed[i], position[i]))
        sEtaPos = sorted(etaPos, key=lambda el: el[1], reverse=True)

        stack = []
        for el in sEtaPos:
            cEta, cPos = el[0], el[1]
            if stack and cEta <= stack[-1][0]:
                continue
            stack.append(el)
        
        return len(stack)