editop
======

Given a pair of source and target strings, we want to compute the
series of edit operations which will transform source to target. We
may also want to align these edit operations with the symbols of the
source string, for example in order to train a sequence model to do
string transduction. This method is used for normalizing tweets in
[1].

Example
-------

    >>> ops = align("c wat", "see what") # Compute edit operations
    >>> "".join(apply(ops, "c wat"))     # Apply them to source string
    'see what'
    >>> for char, op in zip("c wat", ops):  # Inspect the aligned operations
    ...   print repr(char), op
    ... 
    'c' Op({'insert': ['s', 'e', 'e'], 'delete': True})
    ' ' Op({'insert': [], 'delete': False})
    'w' Op({'insert': [], 'delete': False})
    'a' Op({'insert': ['h'], 'delete': False})
    't' Op({'insert': [], 'delete': False})

References
----------

- [1] [Grzegorz Chrupała. 2014. Normalizing tweets with edit scripts and
    recurrent neural embeddings. ACL.](http://anthology.aclweb.org/P/P14/P14-2111.pdf)

