import math


def is_palindrome_simple(x: int) -> bool:
    s = str(x)
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - (i + 1)]:
            return False
    return True


def is_palindrome(x: int) -> bool:
    len: int = math.ceil(math.log(num, 10))
    half_len: int = math.floor(len / 2.0)

    for i in range(half_len):
        # right_removed = int(x / int(math.pow(10, i)))
        # left_removed = right_removed % int(math.pow(10, 2 * half_len - i))
        leftmost = x % 10
        # rightmost = int(x / int(math.pow(10, 2 * half_len - i)))

        x = int(x / 10)

        print(leftmost)

    return False


if __name__ == "__main__":
    num = 1234321
    result = is_palindrome_simple(num)
    print(f"{num} --> {result}")
