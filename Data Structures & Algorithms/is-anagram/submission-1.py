class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ma_dict = {}
        for c in s:
            if c in ma_dict:
                ma_dict[c] += 1
            else:
                ma_dict[c] = 1
        for c in t:
            if c in ma_dict:
                ma_dict[c] -= 1
            else:
                ma_dict[c] = -1
        for k in ma_dict:
            if ma_dict[k] != 0:
                return False
        return True