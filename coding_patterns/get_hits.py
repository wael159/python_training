from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()   # each item: (timestamp, count)
        self.total = 0

    def _evict(self, t):
        # Remove anything older than 300s window: [t-299, t]
        while self.q and t - self.q[0][0] >= 300:
            _, c = self.q.popleft()
            self.total -= c

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            ts, c = self.q.pop()
            self.q.append((ts, c + 1))
        else:
            self.q.append((timestamp, 1))
        self.total += 1
        self._evict(timestamp)

    def get_hits(self, timestamp: int) -> int:
        self._evict(timestamp)
        return self.total
