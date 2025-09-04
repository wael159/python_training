def is_monotonic_main():
    def is_monotonic(arr):
        increasing = decreasing = True
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                decreasing = False
            elif arr[i] < arr[i - 1]:
                increasing = False
        return increasing or decreasing

    print(is_monotonic([1, 2, 2, 3]))  # True
    print(is_monotonic([6, 5, 4, 4]))  # True
    print(is_monotonic([1, 3, 2]))     # False
    print(is_monotonic([1]))           # True
    print(is_monotonic([]))            # True


def is_monotonic_followup1():
    def is_strict_monotonic(arr):
        filtered = [arr[0]] if arr else []
        for num in arr[1:]:
            if num != filtered[-1]:
                filtered.append(num)0.

        increasing = all(filtered[i] <= filtered[i + 1] for i in range(len(filtered) - 1))
        decreasing = all(filtered[i] >= filtered[i + 1] for i in range(len(filtered) - 1))
        return increasing or decreasing

    print(is_strict_monotonic([1, 2, 2, 3]))  # True
    print(is_strict_monotonic([1, 2, 2, 1]))  # False
    print(is_strict_monotonic([3, 3, 3]))     # True


def is_monotonic_followup2():
    class StreamingMonotonicChecker:
        def __init__(self):
            self.last = None
            self.direction = None
            self.valid = True

        def process(self, num):
            if not self.valid:
                return False

            if self.last is not None:
                if num > self.last:
                    if self.direction == 'dec':
                        self.valid = False
                    self.direction = self.direction or 'inc'
                elif num < self.last:
                    if self.direction == 'inc':
                        self.valid = False
                    self.direction = self.direction or 'dec'
            self.last = num
            return self.valid

    stream = StreamingMonotonicChecker()
    data = [1, 2, 2, 3]
    print(all(stream.process(x) for x in data))  # True

    stream = StreamingMonotonicChecker()
    data = [1, 3, 2]
    print(all(stream.process(x) for x in data))  # False


if __name__ == "__main__":
    # print("Main Function:")
    # is_monotonic_main()

    print("\nFollow-up 1:")
    is_monotonic_followup1()
    #
    # print("\nFollow-up 2:")
    # is_monotonic_followup2()
