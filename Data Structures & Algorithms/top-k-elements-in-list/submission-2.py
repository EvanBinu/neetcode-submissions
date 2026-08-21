import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0)+1
        for num in freq.keys():
            heapq.heappush(heap,(freq[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result