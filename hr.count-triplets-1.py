def get_triplet_count(a, d):
    count = 0
    is_triplet = lambda i, j, k: (a[i] + a[j] + a[k]) % d == 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if is_triplet(i, j, k):
                    count += 1

    return count


from itertools import combinations


def get_triplet_count_functional(a, d):
    return sum(1 for i, j, k in combinations(range(len(a)), 3) if (a[i] + a[j] + a[k]) % d == 0)


print(get_triplet_count_functional([2, 3, 1, 6], 3))
