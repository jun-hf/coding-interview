"""
Find a happy number

Eventually things will go back to a cycle, this means we can use fast and slow pointer to determine if the list has a cycle.

first you want to define sum of square,
def sum_square(sum):
    _sum = 0
    as long as num != 0:
        have dig = num modulos 10 to get the last digit
        dig * dig add it to _sum
        num //= 10
    return _sum

ones you have design the sum of square funstions is just like solving slow fast to detect a cycle

def is_happy_number(num):
    slow, fast = num, num

    while fast != 1:
        slow equal to sum_square(num)
        fast call sum_square twice
        if slow == fast:
            return False

    return 1
    
"""

def sum_square(num):
    _sum = 0
    while num != 0:
        dig = num % 10
        _sum += dig * dig
        num //= 10
    return _sum
"""
slow = 8, 64
fast = 8, 52


"""
def is_happy_num(num):
    slow, fast = num, num

    while True:
        
        fast = sum_square(sum_square(fast))
        slow = sum_square(slow)
        print(slow, fast)
        if slow == fast:
            break
    
    return True

print(is_happy_num(8))