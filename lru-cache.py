# -*- coding: utf-8 -*-
import queue


class LRUCache:

    def __init__(self, capacity: int):
        self.table = dict()
        self.priority_cache = dict()
        self.priority = 0
        self.q = queue.PriorityQueue(capacity)

    def get(self, key: int) -> int:
        v = self.table.get(key, -1)
        if v != -1:
            self.priority_cache[key] = self.priority
            self.priority += 1
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table[key] = value
            self.priority_cache[key] = self.priority
            self.priority += 1
            return
        if len(self.table) == self.q.maxsize:
            while True:
                k = self.q.get()[1]
                priority = self.priority_cache.pop(k, None)
                if priority is None:
                    break
                self.q.put((priority, k))
            del self.table[k]
        self.table[key] = value
        self.q.put((self.priority, key))
        self.priority += 1


if __name__ == '__main__':
    c = LRUCache(3)
    c.put(1, 1)
    c.put(2, 2)
    c.put(3, 3)
    c.put(4, 4)
    print(c.get(4))
    print(c.get(3))
    print(c.get(2))
    print(c.get(1))
    c.put(5, 5)
    print(c.get(1))
    print(c.get(2))
    print(c.get(3))
    print(c.get(4))
    print(c.get(5))

