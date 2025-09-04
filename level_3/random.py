import time

class MyRandom:
    def __init__(self, seed=None):
        if seed is None:
            # use current time as seed for different results every run
            seed = int(time.time_ns()) & 0xFFFFFFFF
        self.state = seed

    def random(self):
        # Linear Congruential Generator (LCG) constants
        a = 1664525
        c = 1013904223
        m = 2**32
        self.state = (a * self.state + c) % m
        return self.state / m  # float in [0, 1)

    def choice_10(self):
        return int(self.random() * 10)  # number 0–9 inclusive


# Example usage
gen = MyRandom()
for _ in range(10):
    print(gen.choice_10())
