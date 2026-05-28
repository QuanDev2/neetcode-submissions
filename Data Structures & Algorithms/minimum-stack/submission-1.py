class MinStack:
    """
        O(n): time
        O(n): space
    """
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if self.minStack:
    #         minVal = min(val, self.minStack[-1])
    #     else:
    #         minVal = val
    #     self.minStack.append(minVal)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minStack[-1]

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            diff = val - self.min
            self.stack.append(diff)
            if diff < 0:
                self.min = val
        # [3, 2, 1, 5]
        # min = 1
        # [0, -1, -1, 4]

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

