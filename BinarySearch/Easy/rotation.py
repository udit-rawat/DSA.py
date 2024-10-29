class Solution:
    def findKRotation(self, arr: list[int]) -> int:
        # code here
        low = 0
        high = len(arr)-1
        while low < high:
            mid = (low+high)//2
            if arr[mid] > arr[high]:
                low = mid + 1
            elif arr[mid] <= arr[high]:
                high = mid
        return low
