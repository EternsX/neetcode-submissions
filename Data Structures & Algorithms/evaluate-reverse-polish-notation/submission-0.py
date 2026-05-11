class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(b / a),
        }

        stack = []

        for c in tokens:
            if c in ops:
                stack.append(ops[c](stack.pop(), stack.pop()))
            else:
                stack.append(int(c))
        return stack[-1] if stack else 0