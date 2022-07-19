"""
Given the head of a linkedlist with a cycle, find the start of the cycle

Ones the fast and slow pointer meet, re initialize the fast pointer to the start and move both pointer forward with one step,
the point that they meet is the start of the linked list
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_start_cycle_linked_list(head):
    fast, slow = head, head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break
    
    fast = head

    while True:
        fast = fast.next
        slow = slow.next

        if fast == slow:
            break
    return slow

def main():
    head = Node(9)
    head.next = Node(10)
    head.next.next = Node(8)
    head.next.next = Node(88)
    head.next.next.next = Node(87)
    head.next.next.next.next = Node(9)

    head.next.next.next.next.next = head.next.next

    print(find_start_cycle_linked_list(head).val)
    

main()

