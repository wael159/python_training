# Install before running: pip install intervaltree
from intervaltree import Interval, IntervalTree

# ------------------------------
# Main Question: Any intersection (even point or edge)
# ------------------------------
def rectangles_intersect(rect1, rect2):
    x1_1, y1_1, x2_1, y2_1 = rect1
    x1_2, y1_2, x2_2, y2_2 = rect2

    if x2_1 < x1_2 or x2_2 < x1_1:
        return False
    if y2_1 < y1_2 or y2_2 < y1_1:
        return False

    return True

# ------------------------------
# Follow-up 1: Only if they strictly overlap (not touch)
# ------------------------------
def rectangles_strictly_intersect(rect1, rect2):
    x1_1, y1_1, x2_1, y2_1 = rect1
    x1_2, y1_2, x2_2, y2_2 = rect2

    if x2_1 <= x1_2 or x2_2 <= x1_1:
        return False
    if y2_1 <= y1_2 or y2_2 <= y1_1:
        return False

    return True

# ------------------------------
# Follow-up 2: Stream checker (brute-force)
# ------------------------------
class RectangleStreamChecker:
    def __init__(self):
        self.rectangles = []

    def add_and_check(self, rect):
        for existing in self.rectangles:
            if rectangles_strictly_intersect(existing, rect):
                return True
        self.rectangles.append(rect)
        return False

# ------------------------------
# Follow-up 2 (optimized): Stream checker using Interval Tree
# ------------------------------
class RectangleIndex:
    def __init__(self):
        self.tree = IntervalTree()
        self.rectangles = {}  # Interval → rect tuple

    def add_and_check(self, rect):
        x1, y1, x2, y2 = rect

        # Step 1: query x-overlapping intervals
        overlapping = self.tree.overlap(x1, x2)

        # Step 2: check y-overlaps manually
        for iv in overlapping:
            r2 = self.rectangles[iv]
            if self._y_overlap(rect, r2):
                return True

        # Step 3: add to tree and mapping
        interval = Interval(x1, x2)
        self.tree.add(interval)
        self.rectangles[interval] = rect
        return False

    def _y_overlap(self, r1, r2):
        _, y1_1, _, y2_1 = r1
        _, y1_2, _, y2_2 = r2
        return not (y2_1 <= y1_2 or y2_2 <= y1_1)

# ------------------------------
# Testing all implementations
# ------------------------------
if __name__ == "__main__":
    # print("=== Main Function: rectangles_intersect ===")
    # print(rectangles_intersect((0, 0, 2, 2), (1, 1, 3, 3)))  # True
    # print(rectangles_intersect((0, 0, 1, 1), (1, 1, 2, 2)))  # True (touch)
    # print(rectangles_intersect((0, 0, 1, 1), (2, 2, 3, 3)))  # False
    #
    # print("\n=== Follow-up 1: rectangles_strictly_intersect ===")
    # print(rectangles_strictly_intersect((0, 0, 2, 2), (1, 1, 3, 3)))  # True
    # print(rectangles_strictly_intersect((0, 0, 1, 1), (1, 1, 2, 2)))  # False
    # print(rectangles_strictly_intersect((0, 0, 1, 1), (2, 2, 3, 3)))  # False
    #
    # print("\n=== Follow-up 2: Brute-force Stream Checker ===")
    # checker = RectangleStreamChecker()
    # print(checker.add_and_check((0, 0, 2, 2)))  # False
    # print(checker.add_and_check((3, 3, 4, 4)))  # False
    # print(checker.add_and_check((1, 1, 3, 3)))  # True (overlaps with first)
    # print(checker.add_and_check((5, 5, 6, 6)))  # False

    print("\n=== Follow-up 2 Optimized: Interval Tree Checker ===")
    tree_checker = RectangleIndex()
    print(tree_checker.add_and_check((0, 0, 2, 2)))  # False
    print(tree_checker.add_and_check((3, 3, 4, 4)))  # False
    print(tree_checker.add_and_check((1, 1, 3, 3)))  # True
    print(tree_checker.add_and_check((5, 5, 6, 6)))  # False
