from double_linked_list import DoubleLinkedList


class Queue:
    def __init__(self):
        self._list = DoubleLinkedList()

    def enqueue(self, obj):
        self._list.push(obj)

    def count(self):
        return self._list.count()

    def dequeue(self):
        return self._list.popleft()

    def first(self):
        return self._list.first()

    def last(self):
        return self._list.last()

    def dump(self, mark="-----"):
        self._list.dump(mark)
