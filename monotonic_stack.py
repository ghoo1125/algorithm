# Find the latest greater/less (and equal) than value to the left/right (4 combinations) with time complexity O(n)

if __name__ == '__main__':
    nums = [4, 3, 1, 8, 4, 3, 2, 9, 0, 5, 3]
    # nums = [17, 18, 5, 4, 6, 1]
    n = len(nums)

    left_less_mono = [-1] * n
    stk = []
    for i in range(n):
        while stk and nums[i] < nums[stk[-1]]:
            stk.pop()
        left_less_mono[i] = stk[-1] if stk else -1
        stk.append(i)
    print(nums)
    print(left_less_mono)


    right_greater_mono = [-1] * n
    stk = []
    for i in range(n)[::-1]:
        while stk and nums[i] > nums[stk[-1]]:
            stk.pop()
        right_greater_mono[i] = stk[-1] if stk else -1
        stk.append(i)
    print(nums)
    print(right_greater_mono)
