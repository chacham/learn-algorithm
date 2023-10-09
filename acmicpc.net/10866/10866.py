import sys
input = sys.stdin.readline
print = sys.stdout.write

class deque:
    def __init__(self, size):
        self._start = 0
        self._end = 0
        self._size = 0
        self._maxSize = size
        self._deque = [None] * size
    def push_front(self, item):
        if self._size >= self._maxSize:
            return
        self._deque[self._start] = item
        self._start -= 1
        if self._start < 0:
            self._start += self._maxSize
        self._size += 1
    def pop_front(self):
        if self._size <= 0:
            return -1
        self._start += 1
        if self._start >= self._maxSize:
            self._start -= self._maxSize
        self._size -= 1
        return self._deque[self._start]
    def push_back(self, item):
        if self._size >= self._maxSize:
            return
        self._end += 1
        if self._end >= self._maxSize:
            self._end -= self._maxSize
        self._deque[self._end] = item
        self._size += 1
    def pop_back(self):
        if self._size <= 0:
            return -1
        ret = self._deque[self._end]
        self._end -= 1
        if self._end < 0:
            self._end += self._maxSize
        self._size -= 1
        return ret
    def size(self):
        return self._size
    def empty(self):
        return True if self._size == 0 else False
    def front(self):
        if self._size <= 0:
            return -1
        tmp = self._start + 1
        if tmp >= self._maxSize:
            tmp -= self._maxSize
        return self._deque[tmp]
    def back(self):
        if self._size <= 0:
            return -1
        return self._deque[self._end]

if __name__ == "__main__":
    N = int(input().strip())
    mydeq = deque(N)
    for n in range(N):
        op = input().split()
        if op[0] == "push_front":
            mydeq.push_front(op[1])
        elif op[0] == "push_back":
            mydeq.push_back(op[1])
        elif op[0] == "pop_front":
            print(str(mydeq.pop_front()))
            print('\n')
        elif op[0] == "pop_back":
            print(str(mydeq.pop_back()))
            print('\n')
        elif op[0] == "size":
            print(str(mydeq.size()))
            print('\n')
        elif op[0] == "empty":
            print("1" if mydeq.empty() else "0")
            print('\n')
        elif op[0] == "front":
            print(str(mydeq.front()))
            print('\n')
        elif op[0] == "back":
            print(str(mydeq.back()))
            print('\n')
