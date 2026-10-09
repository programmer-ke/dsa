from dictionary import Dictionary


def test_set_and_get():
    d = Dictionary()
    d.set("a", 1)
    assert d.get("a") == 1


def test_get_missing_returns_default():
    d = Dictionary()
    assert d.get("missing", "fallback") == "fallback"


def test_get_missing_returns_none_without_default():
    d = Dictionary()
    assert d.get("missing") is None


def test_set_overwrites_existing_key():
    d = Dictionary()
    d.set("a", 1)
    d.set("a", 2)
    assert d.get("a") == 2


def test_delete_removes_key():
    d = Dictionary()
    d.set("a", 1)
    d.delete("a")
    assert d.get("a") is None


def test_delete_missing_key_does_not_raise():
    d = Dictionary()
    d.delete("does_not_exist")


def test_list_returns_stored_values():
    d = Dictionary()
    d.set("a", 1)
    d.set("b", 2)
    assert sorted(d.list()) == [1, 2]


def test_list_empty():
    d = Dictionary()
    assert d.list() == []


def test_list_updates_after_set_and_delete():
    d = Dictionary()
    d.set("a", 1)
    d.set("b", 2)
    d.delete("a")
    d.set("c", 3)
    assert sorted(d.list()) == [2, 3]


def test_stored_none_value_is_distinct_from_missing_key():
    sentinel = object()
    d = Dictionary()
    d.set("a", None)
    # If "a" were missing, get would return sentinel.
    assert d.get("a", sentinel) is None


def test_supports_different_key_types():
    d = Dictionary()
    d.set(1, "int")
    d.set("key", "str")
    d.set((1, 2), "tuple")
    assert d.get(1) == "int"
    assert d.get("key") == "str"
    assert d.get((1, 2)) == "tuple"


def test_many_set_and_get():
    d = Dictionary()
    n = 10000
    for i in range(n):
        d.set(i, i * 2)
    for i in range(n):
        assert d.get(i) == i * 2


def test_many_delete():
    d = Dictionary()
    n = 10000
    for i in range(n):
        d.set(i, i)
    for i in range(n):
        d.delete(i)
    assert d.list() == []


def test_many_overwrite():
    d = Dictionary()
    n = 10000
    for i in range(n):
        d.set(i, i)
    for i in range(n):
        d.set(i, i + 1)
    for i in range(n):
        assert d.get(i) == i + 1


if __name__ == "__main__":
    test_many_set_and_get()
    test_many_delete()
    test_many_overwrite()
