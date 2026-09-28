class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy_mappy = {}
        crt_idx = 0
        res = []

        for s in strs:
            alpha = [0] * 26 # 26 letters in the alphabet. Input is only lowercasee letters.
            for c in s:
                alpha[ord(c) - ord('a')] += 1 # compute freq of letters for current string
            
            key = tuple(alpha) # use alpabet array as hash key

            if key in hashy_mappy:
                res[hashy_mappy[key]].append(s) # key exists, it's anagram therfore append to anagram sub-list 
            else:
                hashy_mappy[key] = crt_idx # new string, new sub-list
                res.append([s]) # append new sublist
                crt_idx += 1 # increment current index for future ref
        return res
            

