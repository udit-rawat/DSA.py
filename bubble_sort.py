def count_swaps(arr, ascending=True):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count


def min_swaps_to_beautiful(arr):
    asc_arr = arr[:]
    desc_arr = arr[:]

    asc_swaps = count_swaps(asc_arr, ascending=True)

    desc_swaps = count_swaps(desc_arr, ascending=False)

    return min(asc_swaps, desc_swaps)


N = int(input())
arr = list(map(int, input().split()))

print(min_swaps_to_beautiful(arr))
