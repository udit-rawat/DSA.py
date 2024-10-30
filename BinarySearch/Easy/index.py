class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    high = mid - 1  # Move left to find the first occurrence
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_occurrence

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    low = mid + 1  # Move right to find the last occurrence
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last_occurrence

        # Find the first and last occurrence using binary search
        first_occurrence = findFirst(nums, target)
        last_occurrence = findLast(nums, target)

        return [first_occurrence, last_occurrence]
