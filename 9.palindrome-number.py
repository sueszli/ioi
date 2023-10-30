import math


def is_palindrome(x: int) -> bool:
    len: int = math.ceil(math.log(num, 10))
    half_len: int = math.floor(len / 2.0)

    for i in range(half_len):
        mask = int(math.pow(10, i))
        print(mask)

    return False


if __name__ == "__main__":
    num = 1234567
    result = is_palindrome(num)
    print(f"{num} --> {result}")
