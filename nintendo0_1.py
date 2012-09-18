# -*- coding: utf-8 -*-
#
# nintendo.py
# created by giginet on 2012/09/15
#
def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    for a in xrange(10000):
        if '' != lets_take_tea_break(*[int(i) for i in (a, 17, 3569, 915)]):
            print a
