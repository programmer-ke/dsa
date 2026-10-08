from single_linked_list import SingleLinkedList


class Stack:
    def __init__(self):
        self._list = SingleLinkedList()

    def push(self, obj):
        self._list.push(obj)

    def pop(self):
        return self._list.pop()

    def top(self):
        return self._list.last()

    def count(self):
        return self._list.count()

    def dump(self, mark="----"):
        self._list.dump(mark)
