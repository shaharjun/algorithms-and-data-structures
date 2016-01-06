def check_if_sorted(array, n):
    if n == 1:
        return 1
    return 0 if array[n-1] < array[n-2] else check_if_sorted(array, n-1)

array = [1, 3, 4, 6, 7]
n = check_if_sorted(array, len(array))
if n:
    print("sorted")
else:
    print("not sorted")
