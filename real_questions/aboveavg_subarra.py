def aboveAverageSubarrays(A):
    if not A:
        return []  # no subarrays

    n = len(A)
    total_sum = sum(A)

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]

    result = []
    for l in range(n):
        for r in range(l, n):
            sub_sum = prefix_sum[r + 1] - prefix_sum[l]
            length = r - l + 1

            if length < n:
                # x/k > S/n  <=>  x*n > k*S (integer-safe)
                if sub_sum * n > length * total_sum:
                    result.append([l + 1, r + 1])
            else:
                # whole array vs empty remainder (avg 0)
                if total_sum > 0:
                    result.append([l + 1, r + 1])

    return result
