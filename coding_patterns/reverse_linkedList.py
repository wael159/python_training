class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def revere_linked_list(head):
        prev=None
        curr=head
        while curr:
            next_node = curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev

# Build 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))

# Reverse
new_head = reverse_linked_list(head)

# Print reversed list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output: 3 -> 2 -> 1 ->
