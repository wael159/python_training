from typing import List

# ----------------------
# Main Function
# ----------------------
def missing_number_main():
    def missing_number(nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # Test cases
    print(missing_number([3, 0, 1]))         # → 2
    print(missing_number([0, 1]))            # → 2
    print(missing_number([9,6,4,2,3,5,7,0,1]))  # → 8
    print(missing_number([1]))               # → 0
    print(missing_number([0]))               # → 1

# ----------------------
# Follow-up 1: Constant Space, No Extra Memory
# ----------------------
def missing_number_followup1():
    def missing_number(nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # Test cases
    print(missing_number([3, 0, 1]))         # → 2
    print(missing_number([0, 1]))            # → 2
    print(missing_number([9,6,4,2,3,5,7,0,1]))  # → 8

# ----------------------
# Follow-up 2: Streaming Input
# ----------------------
def missing_number_followup2():
    """
    Optimize for streaming: if you had to process millions of entries one-by-one,
    how would you keep track of the current missing number without storing the full list?
    """

    class MissingNumberStreamProcessor:
        def __init__(self, n):
            self.n = n
            self.expected_sum = n * (n + 1) // 2
            self.actual_sum = 0
            self.count = 0

        def process(self, num):
            self.actual_sum += num
            self.count += 1

        def get_missing(self):
            return self.expected_sum - self.actual_sum

    # Simulate stream
    stream = [0, 1, 2, 4, 5]
    n = 5  # because range is 0 to 5 (6 numbers), one is missing

    processor = MissingNumberStreamProcessor(n)
    for num in stream:
        processor.process(num)

    print(processor.get_missing())  # → 3

# ----------------------
# Run All
# ----------------------
if __name__ == "__main__":
    print("Main Function:")
    missing_number_main()

    print("\nFollow-up 1 (XOR Optimization):")
    missing_number_followup1()

    print("\nFollow-up 2 (Streaming Input):")
    missing_number_followup2()
