def bitonic_sequence(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            return None
        if mid == len(A) - 1:
            return None
        if A[mid - 1] <= A[mid] and A[mid + 1] >= A[mid]:
            low = mid + 1
        elif A[mid - 1] >= A[mid] and A[mid + 1] <= A[mid]:
            high = mid - 1
        elif A[mid - 1] <= A[mid] and A[mid + 1] <= A[mid]:
            return A[mid]
    return None


print(bitonic_sequence([1, 2, 4, 6, 4, 3, 2, 1]))

