from queue import Queue


def test_enqueue():
    q = Queue()
    q.enqueue("A")
    assert q.count() == 1
    q.enqueue("B")
    assert q.count() == 2


def test_dequeue():
    q = Queue()
    q.enqueue("first")
    q.enqueue("second")
    assert q.dequeue() == "first"
    assert q.dequeue() == "second"
    assert q.dequeue() is None


def test_first():
    q = Queue()
    assert q.first() is None
    q.enqueue("X")
    assert q.first() == "X"
    q.enqueue("Y")
    assert q.first() == "X"  # first should remain the oldest item
    q.dequeue()
    assert q.first() == "Y"


def test_last():
    q = Queue()
    assert q.last() is None
    q.enqueue("X")
    assert q.last() == "X"
    q.enqueue("Y")
    assert q.last() == "Y"  # last is the most recently added item
    q.dequeue()
    assert q.last() == "Y"


def test_count():
    q = Queue()
    assert q.count() == 0
    q.enqueue(1)
    q.enqueue(2)
    assert q.count() == 2
    q.dequeue()
    assert q.count() == 1
    q.dequeue()
    assert q.count() == 0


def test_fifo_order():
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    assert q.count() == 5
    for i in range(5):
        assert q.dequeue() == i
    assert q.count() == 0
    # after emptying, enqueue again
    q.enqueue("new")
    assert q.first() == "new"
    assert q.last() == "new"
    assert q.count() == 1


def test_dump():
    # Just ensure it runs without error (no assertion on printed output)
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.dump("test dump")
