# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    # assuming that all this number can be divided by 11, so we can maybe create a list of all the numbers which can be diveded by 11 up to B
    if A == B:
        return 1
    count = sum(1 for i in range(A, B + 1) if len(set(str(i))) == 1)

    return count

def count_uniform_digit_numbers(A, B):
    count = 0
    for digit in range(1, 10):
        num_str = str(digit)
        while True:
            num = int(num_str)
            if num > B:
                break
            if num >= A:
                count += 1
            num_str += str(digit)  # make next: 1 → 11 → 111...
    return count

def count_uniform_digit_numbers(A, B):
    count = 0
    for digit in range(1, 10):  # digits 1 to 9
        num = digit
        while num <= B:
            if num >= A:
                count += 1
            num = num * 10 + digit  # e.g., 1 → 11 → 111 → 1111
    return count


