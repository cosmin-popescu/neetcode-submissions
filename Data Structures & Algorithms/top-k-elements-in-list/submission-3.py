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
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freqs = defaultdict(int)
    #     ma_heap = []
    #     res = []

    #     # count frequencies
    #     for n in nums:
    #         freqs[n] += 1

    #     # append to heap and keep only k items
    #     for f in freqs:
    #         heapq.heappush(ma_heap, (freqs[f], f)) #min heap by default
    #         if len(ma_heap) > k:
    #             heapq.heappop(ma_heap)

    #     for _ in range(k):
    #         res.append(heapq.heappop(ma_heap)[1])

    #     return res

    #var3: bucket grouping
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        buckits = [[] for _ in range(len(nums) + 1)] # because max frequency is len(nums)
        res = []

        # count frequencies in map
        for num in nums:
            counts[num] += 1

        # group frequencies buckets by appearance count
        for num in counts:
            buckits[counts[num]].append(num)

        #extract top k:
        for b in buckits[::-1]:
            for i in b:
                res.append(i)
                if len(res) == k:
                    return res
