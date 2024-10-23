arr = [10, 5, 2, 7, 1, 9]
k = 15
arr = sorted(arr)
sum = 0
idx = 0
for i in range(len(arr)):
    sum += arr[i]
    if sum == k:
        idx = i
print(arr[:i-1])
