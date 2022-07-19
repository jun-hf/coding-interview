"""
Given a haed of the linked list, write a method that check if the given linked list
has a cycle.

Design:
I want to have a slow and fast pointer, as long as the fast and slow meet we know that the linked list has a cycle

def has_cycle(head):
    assign slow & fast the head

    while fast != None && slow fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

Write a method that return the lenght of the cycle:

Design:

Ones the the fast and slow pointer meet, we can create a new pointer that start at the slow pointer and start counting unitl the new pointer reach the slow pointer again
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next 

        if slow == fast:
            return slow
    return False

def cycle_length(slow):
    current = slow
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1

        if current == slow:
            break
    
    return cycle_length

def main():
    head = Node(9)
    head.next = Node(10)
    head.next.next = Node(8)
    head.next.next = Node(88)
    head.next.next.next = Node(87)
    head.next.next.next.next = Node(9)

    print(has_cycle(head))

    head.next.next.next.next.next = head.next.next

    print(has_cycle(head))
    print(cycle_length(has_cycle(head)))
    

main()