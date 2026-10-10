"""Binary search tree implementation"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class BSTNode:
    key: Any
    value: Any
    left: "BSTNode" | None = None
    right: "BSTNode" | None = None


class BST:
    def __init__(self):
        self.root: BSTNode | None = None

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"

    def __iter__(self):
        return self.list()

    def get(self, key: Any) -> Any:
        return self._retrieve(self.root, key)

    def set(self, key: Any, value: Any) -> None:
        self.root = self._insert(self.root, key, value)

    def delete(self, key) -> None:
        self.root = self._delete_from(self.root, key)

    def list(self) -> iter[tuple[Any, Any]]:
        yield from self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return
        if node.left:
            yield from self._preorder(node.left)
        yield (node.key, node.value)
        if node.right:
            yield from self._preorder(node.right)

    def _delete_from(self, node, key):
        if node is None:
            pass
        elif key < node.key:
            node.left = self._delete_from(node.left, key)
        elif key > node.key:
            node.right = self._delete_from(node.right, key)
        else:
            # the current node is to be deleted
            if node.left is None and node.right is None:
                # no children, remove
                node = None
            elif node.left is None:
                # has right child, replace node with right
                node = node.right
            elif node.right is None:
                # has left child, replace node with left
                node = node.left
            else:
                # has both children
                # replace with the largest key, value pair in left subtree
                node.key, node.value = self._get_largest_kv(node.left)
                # delete the old duplicate
                node.left = self._delete_from(node.left, node.key)
        return node

    @staticmethod
    def _get_largest_kv(node):
        """Return the largest value in subtree rooted at node"""
        while node.right:
            node = node.right
        return node.key, node.value

    def _insert(self, node, key, value):
        if node is None:
            node = BSTNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # keys match
            node.value = value
        return node

    def _retrieve(self, node, key):
        if node is None:
            value = None
        elif node.key == key:
            value = node.value
        elif key < node.key:
            value = self._retrieve(node.left, key)
        elif key > node.key:
            value = self._retrieve(node.right, key)
        return value
