from typing import List


class Solution:
    def largest(self, n: int, arr: List[int]) -> int:
        # code here
        # return max(arr)
        maximum = arr[0]
        for i in range(0, n):
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum
