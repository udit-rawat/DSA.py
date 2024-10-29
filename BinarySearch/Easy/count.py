class Solution:
    def count(self, arr, n, x):
        def findFirst(arr, n, x):
            low, high = 0, n - 1
            first_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    first_occurrence = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_occurrence

        def findLast(arr, n, x):
            low, high = 0, n - 1
            last_occurrence = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    last_occurrence = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return last_occurrence

        first_occurrence = findFirst(arr, n, x)
        last_occurrence = findLast(arr, n, x)

        if first_occurrence == -1 or last_occurrence == -1:
            return 0
        else:
            return last_occurrence - first_occurrence + 1
