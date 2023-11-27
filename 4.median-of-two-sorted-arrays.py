from collections import deque

nums1 = [1, 3]
nums2 = [2]

# find median of sorted arrays
merged = []
deque1 = deque(nums1)
deque2 = deque(nums2)
is_empty = lambda d: len(d) == 0

while is_empty(deque1) or is_empty(deque2):
    winner = deque1 if is_empty(deque2) and deque1[0] < deque2[0] else deque2
    winner_val = winner.popleft()
    print(winner_val)
    merged.append(winner_val)

# WIP .......

print(merged)
