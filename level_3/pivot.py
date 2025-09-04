import random

def return_smallest_key_quickselect_iter(inputDict, n):
    if not inputDict or not isinstance(n, int) or n <= 0 or n > len(inputDict):
        return None

    items = list(inputDict.items())  # [(key, value), ...]
    k = n - 1  # zero-based

    def keypair(it):
        return (it[1], it[0])  # (value, key)

    left, right = 0, len(items) - 1
    while True:
        if left == right:
            return items[left][0]

        pivot_index = random.randint(left, right)
        pivot_value = keypair(items[pivot_index])

        # Partition
        i, j = left, right
        while i <= j:
            while keypair(items[i]) < pivot_value:
                i += 1
            while keypair(items[j]) > pivot_value:
                j -= 1
            if i <= j:
                items[i], items[j] = items[j], items[i]
                i += 1
                j -= 1

        if k <= j:
            right = j
        elif k >= i:
            left = i
        else:
            return items[k][0]


def return_smallest_key(inputDict, n):
    # Guard rails
    if not isinstance(n, int) or n <= 0 or not inputDict:
        return None

    # Sort items first by value, then by key (lexicographic)
    items = sorted(inputDict.items(), key=lambda kv: (kv[1], kv[0]))

    # If n is out of range
    if n > len(items):
        return None

    # n-th smallest is at index n-1 after sorting
    return items[n - 1][0]
