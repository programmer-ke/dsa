from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class DoubleLinkedListNode:
    value: Any
    next: "DoubleLinkedListNode" | None = None
    prev: "DoubleLinkedListNode" | None = None


class DoubleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self._count = 0

    def __len__(self):
        return self.count()

    def __iter__(self):
        curr = self.begin
        while curr:
            yield curr.value
            curr = curr.next

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}({[i for i in self]})"

    def push(self, obj):
        """Append a new item to end of list"""
        node = DoubleLinkedListNode(obj)
        if self.end is None:
            # empty list
            self.begin = node
        else:
            self.end.next = node
            node.prev = self.end
        self.end = node
        self._count += 1

    def pop(self):
        """Remove last item and return it"""
        if self.end is None:
            return
        last_value = self.end.value
        self.detach_node(self.end)
        self._count -= 1
        return last_value

    def shift(self, obj):
        """Add items at the beginning of the list"""

        node = DoubleLinkedListNode(obj)
        if self.begin is None:
            # empty list
            self.end = node
        else:
            self.begin.prev = node
            node.next = self.begin

        self.begin = node
        self._count += 1

    def unshift(self):
        """Removes the first item and returns it"""
        if self.begin is None:
            return
        first_value = self.begin.value
        self.detach_node(self.begin)
        self._count -= 1
        return first_value

    def first(self):
        """Returns a reference to the first item"""

        if self.begin:
            return self.begin.value

    def last(self):
        """Returns a reference to the last item"""

        if self.end:
            return self.end.value

    def count(self):
        """Counts number of items in list"""
        return self._count

    def get(self, index):
        """Get the value at index"""

        if index < 0 or index >= len(self):
            return None

        if index < len(self) // 2:
            curr = self.begin
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.end
            for _ in range(len(self) - index - 1):
                curr = curr.prev
        return curr.value

    def dump(self, mark):
        """Dumps the content of the list"""
        print(f"\n{mark}:", end=" ")
        print(self)

    def remove(self, obj):
        """Remove node referencing object and return its index"""
        index, curr = 0, self.begin
        while curr:
            if curr.value == obj:
                self.detach_node(curr)
                self._count -= 1
                return index
            index += 1
            curr = curr.next

    def detach_node(self, node):
        """Detach a node from the list"""

        if node.prev:
            node.prev.next = node.next
        else:
            self.begin = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev
