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

if __name__ == '__main__':
    int = intelligent_data_source_factory(1985, 33067, 84)
    print [int(str(i)) for i in xrange(10)]
