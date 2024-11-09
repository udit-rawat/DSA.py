class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        shifts = []
        original = s
        while True:
            s = s[-1] + s[:-1]
            shifts.append(s)
            if s == original:
                break

        if goal in shifts:
            return True
        else:
            return False
