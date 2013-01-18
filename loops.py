#!/usr/bin/env python
# coding: utf-8


class Nothing(object):
    pass


class Loop(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.count = 0
        self.buffer = []
        self.exhausted = False

    def isfirst(self):
        return self.count == 1

    def islast(self):
        return self.exhausted

    def iseven(self):
        return self.index % 2 == 0

    def false(self, item):
        return isinstance(item, Nothing)

    def isempty(self):
        return (self.count == 0 and self.exhausted)

    def __call__(self, n=1):
        for x in self.iterable:
            self.buffer.append(x)

            if len(self.buffer) > n:
                self.count += 1
                rslt = self.buffer[:n]
                self.buffer = self.buffer[-1:]
                yield rslt if n > 1 else rslt[0]
                self.index += n

        self.exhausted = True
        if 0 < len(self.buffer) <= n:
            rslt = self.buffer + [Nothing] * (n - len(self.buffer))
            self.buffer = []
            self.count += 1
            yield rslt if len(rslt) > 1 else rslt[0]


def loop(iterable, n=1):
    looper = Loop(iterable)
    for x in looper(n):
        yield looper, x
