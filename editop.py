from difflib import *

class Op(object):
    def __init__(self, delete=False, insert=[]):
        self.delete=delete
        self.insert=insert
        
    def rep(self):
        return (self.delete, tuple(self.insert))

    def __repr__(self):
        return "Op({0})".format({'delete':self.delete, 
                                 'insert': self.insert })
    def __hash__(self):
        return hash(self.rep())

    def __cmp__(self, other):
        return cmp(self.rep(), other)

def align(a_, b_):
    '''Align edit operations to each position in the source
    sequence. The sequence of edit operations transforms source
    sequence a to target sequence b.'''
    a = list(a_)
    b = list(b_)
    codes = SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
    T = {}
    for code in codes:
        tag, a_i, a_j, b_i, b_j = code
        if tag in ['insert', 'replace']:
            op = T.get(a_i, Op())
            op.insert = op.insert + b[b_i:b_j]
            T[a_i] = op
        if tag in ['delete', 'replace']:
            for i in range(a_i, a_j):
                op = T.get(i, Op())
                op.delete = True
                T[i] = op
    for i in range(0, len(a)+1):
        if not i in T:
            T[i] = Op()
    return [ op for _, op in sorted(T.iteritems()) ]

def apply(ops, a_):
    '''Apply edit operations ops to source sequence a and return
    a generator for the resulting target sequence.'''
    a = list(a_)
    for i, op in enumerate(ops):
        for x in op.insert + (a[i:i+1] if not op.delete else []):
            yield x

