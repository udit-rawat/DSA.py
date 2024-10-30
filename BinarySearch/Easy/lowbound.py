from typing import List


class Solution:
    # User function Template for python3

    # Complete this function
    # def findFloor(self, A, N, X):
    #     # Your code here
    #     b = True
    #     while b:
    #         A = [item for item in A if item <= X]
    #         if len(A) != 0:
    #             return len(A)-1
    #             b = False
    #         else:

    #             return -1
    #             b = False
    def findFloor(self, A, N, X):
        low = 0
        high = N-1
        ans = N
        while (low <= high):
            mid = (high+low)//2
            if A[mid] >= X:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
