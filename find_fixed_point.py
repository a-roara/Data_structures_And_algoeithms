# T.C = logn, sc -1
def binary_search_fixedpoint(data):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == data[mid]:
            return data[mid]
        elif mid < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search_fixedpoint([1, 2, 2, 5, 7, 9]))

