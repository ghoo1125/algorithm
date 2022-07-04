from bisect import bisect_left, bisect

def binary_search(sorted_arr, target):
    lo, hi = 0, len(sorted_arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] < target:
            lo = mid + 1
        elif sorted_arr[mid] > target:
            hi = mid - 1
        elif sorted_arr[mid] == target:
            return mid
    return -1

def binary_search_bisect(sorted_arr, target):
    i = bisect_left(sorted_arr, target)
    # print(i)
    if i != len(sorted_arr) and sorted_arr[i] == target:
        return i
    else:
        return -1

a = [1, 2, 4, 4, 8]
x = 2
i = binary_search_bisect(a, x)
print(i)
i = binary_search(a, x)
print(i)