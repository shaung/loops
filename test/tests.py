#!/usr/bin/env python
# coding: utf-8

from nose.tools import eq_

from loops import loop, Loop

iterable = xrange(8)

def test_basic():
    eq_([x for l, x in loop(iterable)], list(iterable))
    eq_([l.index for l, x in loop(iterable)], range(len(list(iterable))))
    eq_([l.index for l, x in loop(iterable) if not l.isfirst()], list(iterable)[1:])
    eq_([l.index for l, x in loop(iterable) if not l.islast()], list(iterable)[:-1])
    eq_([l.index for l, x in loop(iterable) if l.iseven()], list(iterable)[::2])

def test_empty():
    l = Loop(range(0))
    for x in l():
        pass
    eq_(l.isempty(), True)

def test_multiitem():
    eq_(sum(((a, b) for l, (a, b) in loop(iterable, n=2)), ()), tuple(iterable))
    eq_([l.index for l, x in loop(iterable, n=2)], range(len(list(iterable)))[::2])


def test_index():
    l = Loop(range(9))
    for x in l(3):
        print l.index, l.count, l.isfirst(), l.islast(), l.iseven(), x
    print l.isempty()

def test_wrapper():
    for l, x in loop(xrange(13)):
        print l.index, l.count, l.isfirst(), l.islast(), l.iseven(), x

if __name__ == '__main__':
    test_index()
    test_wrapper()
