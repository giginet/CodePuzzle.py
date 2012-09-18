class SimpleBars(list):
    def next(self):
        _next = SimpleBars(self)
        for i in xrange(len(self)):
            p = (i - 1) % len(self)
            n = (i + 1) % len(self)
            if self[p] == 'i' and self[i] == 'T' and self[n] == 'i':
                _next[i] = 'i'
            elif self[p] == 'i' and self[i] == 'T':
                _next[i] = ' '
            elif self[i] == 'T' and self[n] == 'i':
                _next[i] = ' '
            elif self[i] == 'T':
                _next[i] = 'i'
            if self[p] == 'i' and self[i] == ' ' and self[n] == 'i':
                _next[i] = ' '
            elif self[p] == 'i' and self[i] == ' ':
                _next[i] = 'i'
            elif self[i] == ' ' and self[n] == 'i':
                _next[i] = 'i'
            elif self[i] == ' ':
                _next[i] = ' '
            if self[i] == 'i':
                _next[i] = 'T'
        for i, c in enumerate(_next):
            self[i] = c
        return self

    def __str__(self):
        return ''.join(self)
    
class Bars(SimpleBars):
    table = [
            {' ' : ' ', 'i' : 'T', 'T' : 'i', 'I' : 'I'},
            {' ' : 'i', 'i' : 'I', 'T' : ' ', 'I' : 'T'}
            ]

    def next(self):
        _next = SimpleBars(self)
        for i in xrange(len(self)):
            p = (i - 1) % len(self)
            n = (i + 1) % len(self)
            if self[p] == 'i' and self[i] == 'T' and self[n] == 'i':
                _next[i] = 'i'
            elif self[p] == 'i' and self[i] == 'T':
                _next[i] = ' '
            elif self[i] == 'T' and self[n] == 'i':
                _next[i] = ' '
            elif self[i] == 'T':
                _next[i] = 'i'
            if self[p] == 'i' and self[i] == ' ' and self[n] == 'i':
                _next[i] = ' '
            elif self[p] == 'i' and self[i] == ' ':
                _next[i] = 'i'
            elif self[i] == ' ' and self[n] == 'i':
                _next[i] = 'i'
            elif self[i] == ' ':
                _next[i] = ' '
            if self[i] == 'i':
                _next[i] = 'T'
            count = 0
            if self.is_black(self[p]): count += 1
            if self.is_black(self[n]): count += 1
            _next[i] = self.table[count % 2][self[i]]
        for i, c in enumerate(_next):
            self[i] = c
        return self

    @staticmethod
    def is_black(c):
        return c == 'i' or c == 'I'
