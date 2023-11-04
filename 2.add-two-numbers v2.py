from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    assert l1 != None and l2 != None
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    return None


# 21
l1 = ListNode(1)
l1.next = ListNode(2)

# 1
l2 = ListNode(1)

# sum
sum = addTwoNumbers(l1, l2)
while sum != None:
    print(sum.val, end="")
    sum = sum.next
