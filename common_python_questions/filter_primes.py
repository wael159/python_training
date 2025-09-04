import math
from typing import List

# ---------- Helper: Efficient primality check ----------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):  # Only odd divisors
        if n % i == 0:
            return False
    return True

# ---------- Main Function ----------
def filter_primes_main(nums: List[int]) -> List[int]:
    """
    Return all prime numbers in the list, preserving order.
    """
    return [num for num in nums if is_prime(num)]

# ---------- Follow-up 1 ----------
def filter_primes_followup1(nums: List[int]) -> List[int]:
    """
    Return unique prime numbers, sorted in ascending order.
    Ignore negative numbers and duplicates.
    """
    return sorted({num for num in nums if num > 1 and is_prime(num)})

# ---------- Follow-up 2 ----------
def sieve_primes_up_to(n: int) -> List[bool]:
    """
    Return a boolean list where index i is True if i is prime.
    Uses the Sieve of Eratosthenes algorithm.
    """
    is_prime = [False, False] + [True] * (n - 1)  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def filter_primes_followup2(nums: List[int]) -> List[int]:
    """
    Use Sieve of Eratosthenes to filter primes efficiently from a large list.
    """
    if not nums:
        return []
    max_val = max(nums)
    sieve = sieve_primes_up_to(max_val)
    return [num for num in nums if sieve[num]]

if __name__ == "__main__":
    # print("Main Function:")
    # nums1 = [10, 3, 4, 7, 9, 11, 15]
    # print("Input:", nums1)
    # print("Output:", filter_primes_main(nums1))  # [3, 7, 11]
    #
    # print("\nFollow-up 1: (No negatives, no duplicates)")
    # nums2 = [11, 3, -2, 3, 11, 7, 2, 2]
    # print("Input:", nums2)
    # print("Output:", filter_primes_followup1(nums2))  # [2, 3, 7, 11]

    print("\nFollow-up 2: (Optimized with Sieve)")
    nums3 = list(range(30))
    print("Input:", nums3)
    print("Output:", filter_primes_followup2(nums3))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
