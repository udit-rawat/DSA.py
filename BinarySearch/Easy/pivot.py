from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1
        return -1
