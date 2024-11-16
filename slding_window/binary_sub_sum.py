class Solution:
    def numSubarraysWithSum(self, nums, goal):
        sum_count = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum-goal in sum_count:
                result += sum_count[prefix_sum-goal]
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0)+1

        return result
