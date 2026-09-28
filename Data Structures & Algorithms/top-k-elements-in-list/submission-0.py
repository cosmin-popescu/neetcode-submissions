class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        res = []

        # compute frequencies and store in hash map
        for n in nums:
            freqs[n] += 1
        
        # sort based on frequency
        # need an auxilairy array
        arr = []
        for n, f in freqs.items():
            arr.append([f, n])
        arr.sort()

        while 0 < k:
            res.append(arr.pop()[1])
            k -= 1
        
        return res
