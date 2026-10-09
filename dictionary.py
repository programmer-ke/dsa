"""Dictionary implementation"""

from double_linked_list import DoubleLinkedList


class Dictionary:

    NUM_BUCKETS = 256

    def __init__(self):
        self._map = DoubleLinkedList()
        for _ in range(self.NUM_BUCKETS):
            self._map.push(DoubleLinkedList())

    def _bucket_hash(self, key):
        return hash(key) % len(self._map)

    def _get_bucket(self, key):
        return self._map.get(self._bucket_hash(key))

    def _get_slot(self, key):
        bucket, slot = self._get_bucket(key), None
        scanner = bucket.begin
        while scanner:
            k, _ = scanner.value
            if k == key:
                slot = scanner
                break
            scanner = scanner.next
        return bucket, slot

    def get(self, key, default=None):
        """Retrieve the value stored at key"""

        _, slot = self._get_slot(key)
        return slot.value[1] if slot else default

    def set(self, key, value):
        """Set a value for key"""

        bucket, slot = self._get_slot(key)
        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))

    def delete(self, key):
        bucket, slot = self._get_slot(key)
        if slot:
            bucket.detach_node(slot)

    def list(self):
        """lists the values stored in dictionary"""
        return [value for bucket in self._map for key, value in bucket]
