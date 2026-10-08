"""sorting algorithms"""

from double_linked_list import DoubleLinkedList


def bubble_sort(numbers):
    """Optimized bubble sort

    Uses new_n to limit sorting space to unsorted prefix"""
    length = len(numbers)
    n = length
    while n > 1:
        i = 1
        new_n = 0
        node = numbers.begin.next  # second node
        while i < length:
            if node.prev.value > node.value:
                # swap out of order nodes
                node.value, node.prev.value = node.prev.value, node.value
                new_n = i
            node = node.next
            i += 1
        n = new_n


def merge_sort(numbers):

    if len(numbers) <= 1:
        # base case, already sorted
        return

    # split list in half
    left = DoubleLinkedList()
    right = DoubleLinkedList()

    length = len(numbers)
    for _ in range(length // 2):
        left.push(numbers.pop())

    while len(numbers):
        right.push(numbers.pop())

    # recursively split
    merge_sort(left)
    merge_sort(right)

    # merge in order
    merge(numbers, left, right)


def merge(parent, left, right):

    # compare top items from both lists
    while len(left) and len(right):
        if left.first() <= right.first():
            parent.push(left.popleft())
        else:
            parent.push(right.popleft())

    # drain the remaining list
    while len(left):
        parent.push(left.popleft())

    while len(right):
        parent.push(right.popleft())


def quicksort(numbers):

    if len(numbers) <= 1:
        # base case, already sorted
        return

    # use first value as pivot
    pivot = numbers.popleft()

    # partition with list copies
    less = DoubleLinkedList()
    greater = DoubleLinkedList()

    while len(numbers):
        value = numbers.popleft()
        if value <= pivot:
            less.push(value)
        else:
            greater.push(value)

    # recursively sort
    quicksort(less)
    quicksort(greater)

    # merge items in order
    for item in less:
        numbers.push(item)
    numbers.push(pivot)
    for item in greater:
        numbers.push(item)
