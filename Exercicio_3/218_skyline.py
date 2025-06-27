import heapq
from collections import defaultdict
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, H, 0))

        events.sort()

        max_heap = [0]
        active_heights_count = defaultdict(int)
        active_heights_count[0] = 1

        skyline = []
        prev_height = 0

        for x, h_type, R in events:
            if h_type < 0:
                height = -h_type
                heapq.heappush(max_heap, -height)
                active_heights_count[height] += 1
            else:
                height = h_type
                active_heights_count[height] -= 1
            
            while active_heights_count[-max_heap[0]] == 0:
                heapq.heappop(max_heap)

            current_max_height = -max_heap[0]

            if current_max_height != prev_height:
                skyline.append([x, current_max_height])
                prev_height = current_max_height
        
        return skyline