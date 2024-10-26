class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        freq1 = [word1.count(ch) for ch in set(word1)]
        freq2 = [word2.count(ch) for ch in set(word2)]

        return sorted(freq1) == sorted(freq2)
