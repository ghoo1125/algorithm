# right most index as pivot, move value less than pivot to the left
def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

# return ksmallest val
def quick_select(arr, l, r, k):
    if k > 0 and (k <= r - l + 1):
        index = partition(arr, l, r)
    
        if (index - l + 1 == k):
            return arr[index]

        if (index - l + 1 > k):
            return quick_select(arr, l, index - 1, k)
        
        return quick_select(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")
    
    

arr = [7, 10, 4, 3, 20, 15]
k = 3
# print(partition(arr, 0, len(arr) - 1))
# print(arr)
print(quick_select(arr, 0, len(arr) - 1, k)) # 7 is the thrid smallest value in the array
print(arr)