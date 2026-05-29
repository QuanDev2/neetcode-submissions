class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push to stack. if stack-1 is operator, pop op. pop prev 2. do operation. 
        # push result back until stack is empty
        stack = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue
            num2, num1 = stack.pop(), stack.pop()
            res = 0
            if token == '+':
                res = num1 + num2
            elif token == '-':
                res = num1 - num2
            elif token == '*':
                res = num1 * num2
            else:
                res = int(float(num1) / num2)
            stack.append(res)

        return int(stack[0]) 
