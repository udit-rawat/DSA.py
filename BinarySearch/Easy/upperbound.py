class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # Sort the array first
        arr.sort()

        low = 0
        high = len(arr) - 1
        floor = -1
        ceil = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                floor = arr[mid]
                ceil = arr[mid]
                break
            elif arr[mid] < x:
                floor = arr[mid]  # Potential floor found
                low = mid + 1
            else:
                ceil = arr[mid]  # Potential ceiling found
                high = mid - 1

        return [floor, ceil]
