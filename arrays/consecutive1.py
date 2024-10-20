lst = [1, 0, 1, 1, 0, 1]

count = []
series = 0
for item in lst:
    if item == 1:
        series += 1
    else:
        if series > 0:
            count.append(series)
        series = 0


print(count)  # To check the result
