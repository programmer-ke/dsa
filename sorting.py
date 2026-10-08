"""sorting algorithms"""


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
    """Merge sort"""

    count = len(numbers)
    numbers.begin = merge_from(numbers.begin, count)
    # find end
    scanner = numbers.begin
    while scanner.next:
        scanner = scanner.next
    numbers.end = scanner


def merge_from(start, length):
    """Return sorted list starting from given node"""

    if not start.next:
        # base case, single node
        return start

    # find midpoint to split list
    mid = length // 2
    count, scanner = 1, start
    while count < mid:
        scanner = scanner.next
        count += 1

    # split list into two
    right = scanner.next
    scanner.next, right.prev = None, None

    # recursively sort halves
    left = merge_from(start, mid)
    right = merge_from(right, length - mid)

    # merge back sorted halves
    return merge(left, right)


def merge(left, right):
    """Merge the two sorted lists into 1"""

    if left is None:
        return right
    if right is None:
        return left

    if left.value > right.value:
        right.next = merge(left, right.next)
        result = right
    else:
        left.next = merge(left.next, right)
        result = left
    return result
