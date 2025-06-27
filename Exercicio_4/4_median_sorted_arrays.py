from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        total_length = m + n

        low = 0
        high = m

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (total_length + 1) // 2 - partitionX

            max_left_X = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            min_right_X = nums1[partitionX] if partitionX != m else float('inf')

            max_left_Y = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            min_right_Y = nums2[partitionY] if partitionY != n else float('inf')

            if max_left_X <= min_right_Y and max_left_Y <= min_right_X:
                if total_length % 2 == 1:
                    return float(max(max_left_X, max_left_Y))
                else:
                    return float(max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2.0
            
            elif max_left_X > min_right_Y:
                high = partitionX - 1
            else:
                low = partitionX + 1
        
        return -1.0