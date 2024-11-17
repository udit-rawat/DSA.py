from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalpoints = sum(cardPoints[:k])
        max_score = totalpoints
        for i in range(1, k+1):
            totalpoints += cardPoints[-i]-cardPoints[k-1]
            max_score = max(max_score, totalpoints)
        return max_score
