class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(stack[-1] + stack[-2])

        return sum(stack)