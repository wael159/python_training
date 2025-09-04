from collections import OrderedDict
from typing import Optional

# =========================
# Version A: Using OrderedDict
# =========================
class LRUCacheOD:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)  # mark as most recently used
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            # refresh position by deleting then reinserting
            del self.od[key]
        elif len(self.od) == self.cap:
            # evict least recently used (the first item)
            self.od.popitem(last=False)
        self.od[key] = value


# =========================
# Version B: Manual (dict + doubly linked list)
# =========================
class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None

class LRUCache:
    """
    LRU using:
      - dict: key -> node.3
      - doubly linked list: head <-> ... <-> tail
        Most-recent at the TAIL, least-recent at the HEAD.next
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> _Node
        # dummy head/tail to avoid edge cases
        self.head = _Node(0, 0)
        self.tail = _Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- Doubly Linked List helpers ----
    def _add_last(self, node: _Node) -> None:
        """Insert node at the tail (most recent)."""
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node: _Node) -> None:
        """Remove node from its current position."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _pop_first(self) -> _Node:
        """Remove and return the least-recent node (head.next)."""
        lru = self.head.next
        self._remove(lru)
        return lru

    # ---- API ----
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        # move to most recent
        self._remove(node)
        self._add_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            # refresh position
            self._remove(node)
            self._add_last(node)
            return

        if len(self.map) == self.cap:
            evicted = self._pop_first()
            del self.map[evicted.key]

        node = _Node(key, value)
        self.map[key] = node
        self._add_last(node)


# =========================
# Simple Tests
# =========================
def run_basic_scenario(CacheClass):
    cache = CacheClass(2)
    cache.put(1, 1)               # {1=1}
    cache.put(2, 2)               # {1=1, 2=2}
    assert cache.get(1) == 1      # access 1 -> {2=2, 1=1}
    cache.put(3, 3)               # evict 2  -> {1=1, 3=3}
    assert cache.get(2) == -1
    cache.put(4, 4)               # evict 1  -> {3=3, 4=4}
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    return "basic OK"

def run_update_refresh_scenario(CacheClass):
    cache = CacheClass(2)
    cache.put(2, 1)               # {2=1}
    cache.put(2, 2)               # update, stays MRU {2=2}
    assert cache.get(2) == 2      # {2=2}
    cache.put(1, 1)               # {2=2, 1=1}
    cache.put(4, 1)               # evict LRU (2) -> {1=1, 4=1}
    assert cache.get(2) == -1
    return "update/refresh OK"

if __name__ == "__main__":
    # Test OrderedDict version
    print("LRUCacheOD:", run_basic_scenario(LRUCacheOD))
    print("LRUCacheOD:", run_update_refresh_scenario(LRUCacheOD))

    # Test manual linked-list version
    print("LRUCache  :", run_basic_scenario(LRUCache))
    print("LRUCache  :", run_update_refresh_scenario(LRUCache))

    print("All tests passed ✅")
