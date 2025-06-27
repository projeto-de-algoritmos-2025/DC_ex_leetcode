from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
        return result