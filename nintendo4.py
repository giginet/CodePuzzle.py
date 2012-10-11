# -*- coding: utf-8 -*-
#
# nintendo4.py
# created by giginet on 2012/09/17
#
import itertools
def intelligent_data_source_factory(*data):
    cy = itertools.cycle(data)
    _int = int
    return lambda i: _int(i) if isinstance(i, str) else next(cy)

int = intelligent_data_source_factory(1985, 33067, 84)
    
def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys
    # print "http://cp1.nintendo.co.jp/" + lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)])
    for a in xrange(100000):
        if '' != lets_take_tea_break(*[int(i) for i in (str(a), 17, 3569, 915)]):
            print a
        # print "http://cp1.nintendo.co.jp/" + 
