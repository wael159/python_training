from collections import defaultdict

from first_repeating_char import first_repeating_char_main


# Main Question
def count_friends_main():
    friendships = [(1, 2), (2, 3), (3, 4), (1, 3)]
    friend_count = defaultdict(int)

    for a, b in friendships:
        friend_count[a] += 1
        friend_count[b] += 1

    print(dict(friend_count))


# Follow-up 1: ignore duplicates and self-loops
def count_friends_followup1():
    friendships = [(1, 2), (2, 1), (3, 4), (3, 3), (4, 3)]
    friend_count = defaultdict(int)
    seen = set()

    for a, b in friendships:
        if a == b:
            continue  # skip self-loop
        key = tuple(sorted((a, b)))
        if key not in seen:
            seen.add(key)
            friend_count[a] += 1
            friend_count[b] += 1

    print(dict(friend_count))


# Follow-up 2: streaming version
def count_friends_followup2():
    class FriendCounter:
        def __init__(self):
            self.counts = defaultdict(int)
            self.seen_pairs = set()

        def process(self, a, b):
            if a == b:
                return
            pair = tuple(sorted((a, b)))
            if pair not in self.seen_pairs:
                self.seen_pairs.add(pair)
                self.counts[a] += 1
                self.counts[b] += 1

        def get_counts(self):
            return dict(self.counts)

    fc = FriendCounter()
    stream = [(1, 2), (2, 1), (3, 4), (3, 3), (1, 4), (1, 2)]

    for a, b in stream:
        fc.process(a, b)

    print(fc.get_counts())

def frind_Acountss ():
    class FreindCount2:
        def __init__(self):
            self.counts = defaultdict(int)
            self.seen_pair_tmp = set ()
        def process_temp(self, a, b):
            if a == b:
                return
            pair = tuple(sorted((a,b)))
            if pair not in self.seen_pair_tmp:
                self.seen_pair_tmp.add(pair)
                self.counts[a] += 1
                self.counts[b] += 1
        def gt_counts_temp(self):
            return dict(self.counts)
    f_tmp = FreindCount2()
    stream = [(1, 2), (2, 1), (3, 4), (3, 3), (1, 4), (1, 2)]
    for a,b in stream:
        f_tmp.process_temp(a, b)
    print(f_tmp.gt_counts_temp())



# Run tests
if __name__ == "__main__":
    # print("Main Function:")
    # count_friends_main()

    # print("\nFollow-up 1:")
    # count_friends_followup1()
    #
    # print("\nFollow-up 2:")
    # count_friends_followup2()
