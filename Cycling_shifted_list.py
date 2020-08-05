# finding the smallest element
def cyclic_shifted_list(A):
    low = 0
    high = len(A) - 1
    while low < high:
        mid = (low + high) // 2
        if A[mid] <= A[high]:
            high = mid
        elif A[mid] > A[high]:
            low = mid + 1
    return A[low]


print(cyclic_shifted_list([4, 5, 6, 7, 1, 2, 3]))
print(cyclic_shifted_list([2, 3, 4, 5, 6, 7, 1]))
