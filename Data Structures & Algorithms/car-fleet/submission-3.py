class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ma_stack = []

        # sort arrays in descending order of positions and iterate
        for p, s in sorted(zip(position, speed), reverse=True):
            # compute time to destination
            # use float division to take into account cars ariving in the same step as different fleets
            time_to_dest = (target - p) / s

            # first car / empty stack -> first fleet
            if not ma_stack:
                ma_stack.append(time_to_dest)
            else:
                # current car does not catchu up to the fleet in front of it
                if ma_stack[-1] < time_to_dest:
                    # create a new fleet
                    ma_stack.append(time_to_dest)
                else:
                    continue
        
        # number of fleets is stack length
        return len(ma_stack)

