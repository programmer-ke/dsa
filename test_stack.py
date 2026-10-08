from stack import Stack


def test_push():
    s = Stack()
    s.push("A")
    assert s.count() == 1
    s.push("B")
    assert s.count() == 2


def test_pop():
    s = Stack()
    s.push("first")
    s.push("second")
    assert s.pop() == "second"
    assert s.pop() == "first"
    assert s.pop() is None


def test_top():
    s = Stack()
    assert s.top() is None
    s.push("X")
    assert s.top() == "X"
    s.push("Y")
    assert s.top() == "Y"  # top should be the most recently pushed item
    s.pop()
    assert s.top() == "X"


def test_count():
    s = Stack()
    assert s.count() == 0
    s.push(1)
    s.push(2)
    assert s.count() == 2
    s.pop()
    assert s.count() == 1
    s.pop()
    assert s.count() == 0


def test_push_pop_sequence():
    s = Stack()
    for i in range(5):
        s.push(i)
    assert s.count() == 5
    for i in range(4, -1, -1):
        assert s.pop() == i
    assert s.count() == 0
    # after emptying, push again
    s.push("new")
    assert s.top() == "new"
    assert s.count() == 1


def test_dump():
    # Just ensure it runs without error (no assertion on printed output)
    s = Stack()
    s.push("hello")
    s.push("world")
    s.dump("test dump")
