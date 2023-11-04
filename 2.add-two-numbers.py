from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def num_to_list(num: int) -> ListNode:
    root = ListNode(num % 10)
    curr = root

    num = num // 10
    while num != 0:
        curr.next = ListNode(num % 10)
        curr = curr.next
        num = num // 10

    return root


def list_to_num(l: ListNode) -> int:
    assert l != None
    c = 0
    sum = l.val
    while l.next != None:
        l = l.next
        c += 1
        sum += int(l.val + math.pow(10, c))
    return sum


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    assert l1 != None and l2 != None
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    l1_num = list_to_num(l1)
    l2_num = list_to_num(l2)
    return num_to_list(l1_num + l2_num)


def print_list(l: Optional[ListNode]) -> str:
    assert l != None
    string = "list: "
    curr = l
    while curr != None:
        string += f"({curr.val})"
        curr = curr.next
    return string


arg1 = 21
arg2 = 1
result_list = addTwoNumbers(num_to_list(arg1), num_to_list(arg2))
assert result_list != None
print(f"{arg1} + {arg2} = {list_to_num(result_list)}")
