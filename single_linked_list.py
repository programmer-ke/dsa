from __future__ import annotations
from typing import Any
from dataclasses import dataclass


@dataclass
class SingleLinkedListNode:
    value: Any
    next: "SingleLinkedListNode" | None = None


class SingleLinkedList:

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
        node = SingleLinkedListNode(obj)
        if self.end is None:
            # is first item
            self.begin = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
        self._count += 1

    def pop(self):
        """Remove last item and return it"""
        if self.end is None:
            return

        prev, curr = None, self.begin

        # find second-last item
        while curr.next:
            prev = curr
            curr = curr.next

        # Make second last item last
        self.end = prev

        if self.end is None:
            # No nodes left
            self.begin = None
        else:
            # delink previous last item
            self.end.next = None

        self._count -= 1
        return curr.value

    def appendleft(self, obj):
        """Add items at the beginning of the list"""
        node = SingleLinkedListNode(obj, self.begin)
        if self.begin is None:
            # list is empty
            self.end = node

        self.begin = node
        self._count += 1

    def popleft(self):
        """Removes the first item and returns it"""

        if self.begin is None:
            return

        first = self.begin
        self.begin = first.next

        if self.begin is None:
            # list is now empty
            self.end = None

        self._count -= 1
        return first.value

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

        count, curr = 0, self.begin
        while curr:
            if count == index:
                return curr.value
            curr = curr.next
            count += 1

    def dump(self, mark):
        """Dumps the content of the list"""
        print(f"\n{mark}:", end=" ")
        print([i for i in self])

    def remove(self, obj):
        """Remove node referencing object and return its index"""

        index, prev, curr = 0, None, self.begin
        while curr:
            if curr.value == obj:
                # found item to remove
                if prev is None:
                    self.begin = curr.next
                else:
                    prev.next = curr.next

                # update end if necessary
                if curr == self.end:
                    self.end = prev

                self._count -= 1
                return index
            prev, curr = curr, curr.next
            index += 1
