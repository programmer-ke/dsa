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
