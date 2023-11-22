# https://www.codewars.com/kata/596d93bd9b6a5df4de000049


def hash_str(string: str) -> int:
    a: int = sum([ord(char) for char in string])  # char sum
    get_prev_diff = lambda string, i: ord(string[i - 1]) - ord(string[i]) if i != 0 else 0  # diff with previous char
    b: int = sum([get_prev_diff(string, i) for i, _ in enumerate(string)])  # sum of diff with previous char

    # c := (a OR b) AND ((NOT a) shift left by 2 bits)

    return -1


hash_str("peanuts")
