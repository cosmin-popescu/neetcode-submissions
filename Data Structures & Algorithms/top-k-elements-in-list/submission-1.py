class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freqs = defaultdict(int)
    #     res = []

    #     # compute frequencies and store in hash map
    #     for n in nums:
    #         freqs[n] += 1
        
    #     # sort based on frequency
    #     # need an auxilairy array
    #     arr = []
    #     for n, f in freqs.items():
    #         arr.append([f, n])
    #     arr.sort()

    #     while 0 < k:
    #         res.append(arr.pop()[1])
    #         k -= 1
        
    #     return res

    # var2: min-heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        ma_heap = []
        res = []

        # count frequencies
        for n in nums:
            freqs[n] += 1

        # append to heap and keep only k items
        for f in freqs:
            heapq.heappush(ma_heap, (freqs[f], f))
            if len(ma_heap) > k:
                heapq.heappop(ma_heap)

        for _ in range(k):
            res.append(heapq.heappop(ma_heap)[1])

        return res
