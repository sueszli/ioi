from collections import deque


class AddingStack:
    def __init__(self) -> None:
        self.items = deque()

    def push(self, v: int) -> None:
        # push integer on top
        self.items.appendleft(v)

    def pop(self) -> None:
        # pop from top
        self.items.popleft()

    def inc(self, i: int, v: int) -> None:
        # add v to the bottom i elements of the stack
        for j in range(len(self.items) - 1, len(self.items) - i - 1, -1):
            self.items[j] += v

    def empty(self) -> bool:
        # is stack empty?
        return len(self.items) == 0

    def peek(self) -> int:
        # return top
        return self.items[0]

    def sum(self) -> int:
        # return sum of all elements
        return sum(self.items)


def test1():
    stack = AddingStack()
    stack.push(4)
    print(stack.items)
    stack.pop()
    print(stack.items)
    stack.push(3)
    print(stack.items)
    stack.push(5)
    print(stack.items)
    stack.push(2)
    print(stack.items)

    stack.inc(3, 1)
    print(stack.items)
    stack.pop()
    print(stack.items)
    stack.push(1)
    print(stack.items)
    stack.inc(2, 2)
    print(stack.items)

    stack.push(4)
    print(stack.items)
    stack.pop()
    print(stack.items)
    stack.pop()
    print(stack.items)


test1()


# [4]
# []
# [3]
# [3, 5]
# [3, 5, 2]
# [4, 6, 3]
# [4, 6]
# [4, 6, 1]
# [6, 8, 1]
# [6, 8, 1, 4]
# [6, 8, 1]
# [6, 8]
