from bisect import bisect_left, bisect


def binary_search(sorted_arr, target):
    i = bisect_left(sorted_arr, target)
    # print(i)
    if i != len(sorted_arr) and sorted_arr[i] == target:
        return i
    else:
        return -1

a = [1, 2, 4, 4, 8]
x = 9
i = binary_search(a, x)
# print(i)

b = [[1, 3], [2, 4], [3, 2], [4, 6]]
print(bisect(b, [1, 2]))