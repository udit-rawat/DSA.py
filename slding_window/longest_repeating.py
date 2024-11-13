class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxlen = 0
        max_count = 0
        char_count = {}

        for right in range(len(s)):

            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])
            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum length of the window
            maxlen = max(maxlen, right - left + 1)

        return maxlen
