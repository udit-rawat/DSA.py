from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_s = min(len(word) for word in strs)
        char = ""

        for idx in range(min_s):

            current_char = strs[0][idx]
            if all(word[idx] == current_char for word in strs):
                char += current_char
            else:
                break

        return char
