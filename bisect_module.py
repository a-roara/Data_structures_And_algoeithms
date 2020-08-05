# built in binary search
import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# bisect left - find the leftmost occurence
print(bisect.bisect_left(A, 108))

# bisect right - find the index after the right most occurence
# i.e; if found at 8 then the result is 9
print(bisect.bisect_right(A, 285))

# bisect - works same as bisect right
print(bisect.bisect(A, 285))

# insort - inserts while maintaining the order
# insort left - inserts duplicate to left
# insort right - inserts duplicate to right
bisect.insort_left(A, 243)
print(A)
