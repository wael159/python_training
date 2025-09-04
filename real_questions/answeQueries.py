def answerQueries(queries, N):
    result = []
    data = [False] * N  # initialize N booleans

    for op, x in queries:
        if op == 1:
            if 0 <= x < N:
                data[x] = True
        elif op == 2:
            found = -1
            for i in range(x, N):
                if data[i]:
                    found = i
                    break
            result.append(found)

    return result

def binary_search_left(arr, x):
    """Find the leftmost index where x could be inserted (lower bound)."""
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1  # go right
        else:
            high = mid     # go left (or stay)
    return low  # insertion position / first >= x


def answerQueries_2(queries, N):
    true_indices = []  # sorted list of indices set to True
    results = []

    for t, idx in queries:
        if t == 1:
            # SET: mark index as True (store in sorted order)
            pos = binary_search_left(true_indices, idx)
            if pos == len(true_indices) or true_indices[pos] != idx:
                true_indices.insert(pos, idx)  # keep sorted order
        else:
            # GET: find smallest true index >= idx
            pos = binary_search_left(true_indices, idx)
            if pos < len(true_indices):
                results.append(true_indices[pos])
            else:
                results.append(-1)  # nothing found
    return results


# Example usage:
N = 5
queries = [
    [2, 3],  # GET 3 → no true indices yet → -1
    [1, 2],  # SET 2 → true_indices = [2]
    [2, 1]
]# GET 1 → first true

answerQueries_2(queries, N)
