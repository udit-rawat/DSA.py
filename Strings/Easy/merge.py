class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l1 = len(word1)
        l2 = len(word2)
        for i in range(min(l1, l2)):
            result += word1[i]
            result += word2[i]
        if l1 > l2:
            result += word1[l2:]
        else:
            result += word2[l1:]
        return result
