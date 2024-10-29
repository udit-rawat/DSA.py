from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)-1
        target = nums[n]
        low = 0
        high = n
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid] <= nums[high]:
                high = mid

        return nums[low]
