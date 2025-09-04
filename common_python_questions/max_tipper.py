def max_tipper_main():
    """
    Main Question:
    Given a list of (bill, tip) tuples, return the index of the customer who left the highest tip.
    If multiple customers left the same highest tip, return the index of the first one.
    """
    def max_tipper(bills):
        max_tip = -1
        max_index = -1
        for i, (_, tip) in enumerate(bills):
            if tip > max_tip:
                max_tip = tip
                max_index = i
        return max_index

    # Test cases
    bills1 = [(100, 10), (80, 20), (120, 15)]
    bills2 = [(50, 5), (30, 5), (90, 5)]
    bills3 = [(200, 25), (100, 30), (150, 20)]

    print(max_tipper(bills1))  # Expected: 1
    print(max_tipper(bills2))  # Expected: 0 (first with tip 5)
    print(max_tipper(bills3))  # Expected: 1


def max_tipper_followup1():
    """
    Follow-up 1:
    If multiple customers gave the same tip, return the one who paid the highest bill.
    Still return the index in the original list.
    """
    def max_tipper(bills):
        max_tip = -1
        max_bill = -1
        max_index = -1
        for i, (bill, tip) in enumerate(bills):
            if tip > max_tip or (tip == max_tip and bill > max_bill):
                max_tip = tip
                max_bill = bill
                max_index = i
        return max_index

    # Test cases
    bills1 = [(100, 10), (120, 20), (130, 20)]  # tie in tip, pick higher bill (130)
    bills2 = [(50, 5), (60, 5), (30, 5)]
    bills3 = [(200, 30), (190, 30), (210, 29)]

    print(max_tipper(bills1))  # Expected: 2
    print(max_tipper(bills2))  # Expected: 1
    print(max_tipper(bills3))  # Expected: 0


def max_tipper_followup2():
    """
    Follow-up 2:
    Optimize for streaming: if you had to process millions of entries one-by-one,
    how would you keep track of the current max tipper without storing the whole list?
    """
    class MaxTipperTracker:
        def __init__(self):
            self.max_tip = -1
            self.max_bill = -1
            self.max_index = -1
            self.current_index = 0

        def process(self, bill, tip):
            if tip > self.max_tip or (tip == self.max_tip and bill > self.max_bill):
                self.max_tip = tip
                self.max_bill = bill
                self.max_index = self.current_index
            self.current_index += 1

        def get_max_index(self):
            return self.max_index
    # Use the tracker to process the CSV
    tracker = MaxTipperTracker()

    with open("tips.csv") as file:
        for line in file:
            bill, tip = map(float, line.strip().split(","))
            tracker.process(bill, tip)

    print("Best tipper index:", tracker.get_max_index())



def max_tipper_advanced():
    """
    Advanced:
    Handle nested or streaming data like:
    [ {'customer': 'Alice', 'payment': {'bill': 120, 'tip': 30}}, ...]
    Return the customer name who tipped the most, with tie-breaker on highest bill.
    """
    def max_tipper_customers(customers):
        max_tip = -1
        max_bill = -1
        best_customer = None
        for customer in customers:
            bill = customer['payment']['bill']
            tip = customer['payment']['tip']
            name = customer['customer']
            if tip > max_tip or (tip == max_tip and bill > max_bill):
                max_tip = tip
                max_bill = bill
                best_customer = name
        return best_customer

    data = [
        {'customer': 'Alice', 'payment': {'bill': 100, 'tip': 25}},
        {'customer': 'Bob', 'payment': {'bill': 200, 'tip': 25}},
        {'customer': 'Carol', 'payment': {'bill': 180, 'tip': 20}},
    ]

    print(max_tipper_customers(data))  # Expected: Bob


# Test all
if __name__ == "__main__":
    # print("Main Function:")
    # max_tipper_main()
    #
    # print("\nFollow-up 1:")
    # max_tipper_followup1()
    #
    print("\nFollow-up 2:")
    max_tipper_followup2()
    #
    # print("\nAdvanced Extension:")
    # max_tipper_advanced()
