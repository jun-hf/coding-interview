"""
Given a linked list find out the middle of the node.

You can just use fast and slow, given that fast moves twice as fast as slow, when fast reach the end slow will be at the middle

Design:

def middle_list(head):
    slow, fast = head, head

    while (fast and fast.next != None):
        fast = fast.next.next
        slow = slow.next

    if fast != None:
        return slow.next
    
    return slow
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def find_middle_node(head):
    slow, fast = head, head

    while (fast != None and fast.next != None):
        print(slow.val, fast.val)
        slow = slow.next
        fast = fast.next.next
        print("after")
        print(slow.val, fast.val)

    return slow.val

def print_node(head):
    node = head

    while node:
        print(node.val)
        node = node.next


def main():
    head = Node(9)
    head.next = Node(10)
    head.next.next = Node(8)
    head.next.next = Node(88)
    head.next.next.next = Node(87)
    head.next.next.next.next = Node(9)

    #print(find_middle_node(head))
    print(print_node(head))

main()