from random import randint

import sorting
from double_linked_list import DoubleLinkedList

max_numbers = 30


def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.appendleft(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next
    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)
    numbers.dump("after bubble sort")
    assert is_sorted(numbers)


def test_merge_sort():
    numbers = random_list(max_numbers)
    sorting.merge_sort(numbers)
    assert is_sorted(numbers)
