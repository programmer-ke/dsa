"""Tests for binary search tree"""

import random
from bst import BST


def test_set_and_get():
    bst = BST()
    bst.set(10, "apple")
    assert bst.get(10) == "apple"


def test_get_empty_tree():
    bst = BST()
    assert bst.get(5) is None


def test_get_missing_key():
    bst = BST()
    bst.set(1, "one")
    assert bst.get(2) is None


def test_set_overwrites_existing_key():
    bst = BST()
    bst.set(1, "one")
    bst.set(1, "uno")
    assert bst.get(1) == "uno"
    # check no duplicate created
    assert len(list(bst.list())) == 1


def test_set_multiple_keys():
    bst = BST()
    bst.set(5, "five")
    bst.set(3, "three")
    bst.set(7, "seven")
    assert bst.get(3) == "three"
    assert bst.get(5) == "five"
    assert bst.get(7) == "seven"


def test_set_none_value():
    bst = BST()
    bst.set(1, None)
    assert bst.get(1) is None
    assert list(bst.list()) == [(1, None)]


def test_delete_leaf():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.set(3, "c")
    bst.delete(1)
    assert bst.get(1) is None
    assert bst.get(2) == "b"
    assert bst.get(3) == "c"
    assert len(list(bst.list())) == 2


def test_delete_node_with_one_child():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.delete(2)
    assert bst.get(2) is None
    assert bst.get(1) == "a"
    assert len(list(bst.list())) == 1


def test_delete_node_with_two_children():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.set(3, "c")
    bst.delete(2)
    assert bst.get(2) is None
    assert bst.get(1) == "a"
    assert bst.get(3) == "c"
    assert len(list(bst.list())) == 2


def test_delete_root_leaf():
    bst = BST()
    bst.set(1, "a")
    bst.delete(1)
    assert bst.get(1) is None
    assert len(list(bst.list())) == 0


def test_delete_root_with_one_child():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.delete(2)
    assert bst.get(2) is None
    assert bst.get(1) == "a"
    assert len(list(bst.list())) == 1


def test_delete_root_with_two_children():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.set(3, "c")
    bst.delete(2)
    assert bst.get(2) is None
    assert bst.get(1) == "a"
    assert bst.get(3) == "c"
    assert len(list(bst.list())) == 2


def test_delete_missing_key():
    bst = BST()
    bst.set(1, "a")
    bst.delete(99)
    assert bst.get(1) == "a"
    assert len(list(bst.list())) == 1


def test_delete_empty_tree():
    bst = BST()
    bst.delete(1)  # should not raise
    assert len(list(bst.list())) == 0


def test_delete_all():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.set(3, "c")
    bst.delete(1)
    bst.delete(2)
    bst.delete(3)
    assert len(list(bst.list())) == 0


def test_list_empty():
    bst = BST()
    assert list(bst.list()) == []


def test_list_single():
    bst = BST()
    bst.set(5, "five")
    assert list(bst.list()) == [(5, "five")]


def test_list_sorted_order():
    bst = BST()
    bst.set(5, "five")
    bst.set(3, "three")
    bst.set(7, "seven")
    bst.set(1, "one")
    bst.set(4, "four")
    assert list(bst.list()) == [
        (1, "one"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
        (7, "seven"),
    ]


def test_list_after_overwrite():
    bst = BST()
    bst.set(1, "one")
    bst.set(1, "uno")
    assert list(bst.list()) == [(1, "uno")]


def test_list_after_delete():
    bst = BST()
    bst.set(2, "b")
    bst.set(1, "a")
    bst.set(3, "c")
    bst.delete(2)
    assert list(bst.list()) == [(1, "a"), (3, "c")]


def test_many_operations():
    bst = BST()
    for i in range(100):
        bst.set(i, str(i))
    assert bst.get(50) == "50"
    for i in range(0, 100, 2):
        bst.delete(i)
    for i in range(0, 100, 2):
        assert bst.get(i) is None
    for i in range(1, 100, 2):
        assert bst.get(i) is not None


def test_many_set_and_get():
    b = BST()
    n = 10000
    for _ in range(n):
        i = random.randint(1, n)
        b.set(i, i * 2)
    for i in range(n):
        found = b.get(i)
        if found:
            assert found == i * 2


def test_many_delete():
    b = BST()
    n = 10000
    for _ in range(n):
        i = random.randint(1, n)
        b.set(i, i * 2)
    for i in range(1, n + 1):
        b.delete(i)
    assert list(b.list()) == []


def test_many_overwrite():
    b = BST()
    n = 10000
    s = set()
    for _ in range(n):
        i = random.randint(1, n)
        b.set(i, i)
        s.add(i)
    for i in s:
        b.set(i, i + 1)
    for i in s:
        b.get(i) == i + 1


if __name__ == "__main__":
    test_many_set_and_get()
    test_many_delete()
    test_many_overwrite()
