class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans1 = []
        ans2 = []
        ans = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for item in nums1:
            if item not in nums2:
                ans1.append(item)
        ans.append(ans1)
        for item in nums2:
            if item not in nums1:
                ans2.append(item)
        ans.append(ans2)

        return ans
