def binary_search_square_root(target):
    low = 0
    high = target
    while low <= high:
        mid = (low + high) // 2
        square_num = mid ** 2
        if square_num > target:
            high = mid - 1
        elif square_num <= target:
            low = mid + 1
    return low - 1


print(binary_search_square_root(300))
