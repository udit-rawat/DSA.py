class Solution:
    def maxDepth(self, s: str) -> int:
        chars = ["(", ")"]
        count = 0
        temp = 0
        for char in s:
            if char == chars[0]:
                count += 1
                temp = max(count, temp)
            elif char == chars[1]:
                count -= 1

        return temp
