def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2
        left_dif = float("inf")
        right_dif = float("inf")
        if mid > 0:
            left_dif = abs(A[mid - 1] - target)
        if mid + 1 < len(A):
            right_dif = abs(A[mid + 1] - target)
        if left_dif < min_diff:
            min_diff = left_dif
            closest_num = A[mid - 1]
        if right_dif < min_diff:
            min_diff = right_dif
            closest_num = A[mid + 1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            return A[mid]
    return closest_num


print(find_closest_num([2, 5, 6, 7, 8, 8, 9], 8))

