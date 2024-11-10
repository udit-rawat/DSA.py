class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        out = 0
        for i in range(n):
            if i < n-1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                out -= roman_numerals[s[i]]
            else:
                out += roman_numerals[s[i]]
        return out
