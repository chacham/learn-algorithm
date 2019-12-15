from threading import Lock

class Foo:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        for lock in self.locks:
            lock.acquire()
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.locks[0].acquire()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.locks[1].acquire()

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
