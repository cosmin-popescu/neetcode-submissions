class Solution:

    def hash_func(self, c: str):
        return hash(c)

    def isAnagram(self, s: str, t: str) -> bool:
        ma_dict = {}
        for c in s:
            h = hash(c)
            if h in ma_dict:
                ma_dict[h] += 1
            else:
                ma_dict[h] = 1
        for c in t:
            h = hash(c)
            if h in ma_dict:
                ma_dict[h] -= 1
            else:
                ma_dict[h] = -1
        for k in ma_dict:
            if ma_dict[k] != 0:
                return False
        return True