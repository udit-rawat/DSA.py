class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        out = ""
        for value, key in map.items():
            op = value*key
            out += op
        return out
