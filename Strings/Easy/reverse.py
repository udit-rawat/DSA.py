class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for char in s:
            if char != ' ':
                word += char
            elif word:
                words.append(word)
                word = ""

        if word:
            words.append(word)

        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        result = ""
        for i in range(len(words)):
            result += words[i]
            if i < len(words) - 1:
                result += " "

        return result
