from collections import deque

nums1 = [1, 2]
nums2 = [3, 4]


def peekleft(d: deque) -> int | None:
    if len(d) == 0:
        return None
    val = d.popleft()
    d.appendleft(val)
    return val


# def findMedianSortedArrays(nums1, nums2):
#     merged = []
#     deque1 = deque(nums1)
#     deque2 = deque(nums2)

#     is_empty = lambda x: len(x) == 0

#     while pl1 or pl2:
#         pl1 = peekleft(deque1)
#         pl2 = peekleft(deque2)
#         winner = deque1 if (pl1 and pl2 and pl1 < pl2) or (pl1 and not pl2) else deque2
#         winner_val = winner.popleft()
#         merged.append(winner_val)

#     get_median = lambda x: (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2 if len(x) % 2 == 0 else x[len(x) // 2]

#     print(merged)
#     print(get_median(merged))
#     return get_median(merged)
