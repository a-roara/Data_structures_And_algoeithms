def binary_search_firstelem(data, target):
    low = 0
    high = len(data) - 1
    result = None
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            result = mid
            high = mid - 1
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result


print(binary_search_firstelem([-14, -10, 2, 108, 108, 243, 285, 285, 401], 285))

