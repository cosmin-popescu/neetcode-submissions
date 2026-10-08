class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacko = []
        result = [0] * len(temperatures)

        # walk through days left to right
        for i, t in enumerate(temperatures):
            # while we have contents in the stack
            while stacko:
                # if current day temp is higher that what's on the stack top
                if t > temperatures[stacko[-1]]:
                    # pop out the stack top
                    old = stacko.pop()
                    # compute days for the index at the top
                    result[old] = i - old
                else:
                    break
            # append current day to the stack
            stacko.append(i)
        
        return result
        