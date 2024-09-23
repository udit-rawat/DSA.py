class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        num = set(arr)
        value = []
        for item in num:
            value.append(arr.count(item))

        if len(value) == len(set(value)):
            return True
        else:
            False
