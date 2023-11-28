from collections import deque

nums1 = [1, 2, 3, 5]
nums2 = [4]

# find median of sorted arrays
merged = []
deque1 = deque(nums1)
deque2 = deque(nums2)

is_empty = lambda x: len(x) == 0
is_even = lambda x: len(x) % 2 == 0
get_median = lambda x: (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2 if is_even(x) else x[len(x) // 2]

while not is_empty(deque1) or not is_empty(deque2):
    winner = deque1 if is_empty(deque2) or deque1[0] < deque2[0] else deque2
    winner_val = winner.popleft()
    merged.append(winner_val)


print(merged)
print(get_median(merged))
