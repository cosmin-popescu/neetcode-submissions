import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+' : operator.add, 
            '-' : operator.sub, 
            '*' : operator.mul, 
            '/' : lambda a, b: int(a / b)
        }

        stacko = []

        for t in tokens:
            if t not in operators:
                stacko.append(int(t))
            else:
                b = stacko.pop()
                a = stacko.pop()
                stacko.append(operators[t](a, b))

        return stacko.pop()
