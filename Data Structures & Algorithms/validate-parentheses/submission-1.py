class Solution:
    def isValid(self, s: str) -> bool:
        ma_stack = []

        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        mapping = { ')' : '(', ']' : '[', '}' : '{'}

        # iterate characters
        for c in s:
            # is opening bracket - append to stack
            if c in opening:
                ma_stack.append(c)
            # is closing bracket - check for closing bracket in stack
            else:
                if c in closing:
                    # stack not empty
                    if ma_stack:
                        # found matching bracket
                        if ma_stack.pop() == mapping[c]:
                            continue
                        # not match
                        else:
                            return False
                    else:
                        return False

        # stack is not empty
        if ma_stack:
            return False

        return True
                