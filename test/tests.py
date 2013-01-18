#!/usr/bin/env python
# coding: utf-8

from loop import loop, Loop

def test_first():
    l = Loop(range(9))
    for x in l(3):
        print l.index, l.count, l.isfirst(), l.islast(), l.iseven(), x
    print l.isempty()

def test_wrapper():
    for l, x in loop(xrange(13)):
        print l.index, l.count, l.isfirst(), l.islast(), l.iseven(), x

if __name__ == '__main__':
    test_first()
    test_wrapper()
