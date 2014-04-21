# Ch 1 - Python Primer

## 1.1 Python Overview

* Whoa - I didn't know you could 

        python -i demo.py

    This runs the script `demo.py` and then opens up the interpreter in interactive mode.

## 1.2 - Objects in Python

* Ahh, so in python3 you can no longer:
    
        >>> False = 'thing'
          File "<stdin>", line 1
        SyntaxError: assignment to keyword

    (In python2, you can do this, scott free.)

* I didn't know about the `frozenset` type! Does this exist in python2, too, and I just didn't realize?

* I didn't know about defaults:
        
        >>> bool()
        False
        >>> int()
        0
        >>> float()
        0.0
        >>> str()
        ''
* int - Whoa! You can convert ints in non-base 10, like base 16, by giving a second parameter to int:
        
        >>> int('7f', 16)
        127

* float - An error?
        
> If the parameter to the constructor is a string, as with float( 3.14 ), it attempts to parse that string as a floating-point value, raising a ValueError as an exception.

    But we can:

        >>> float('3.14')
        3.14

## 1.3 - Expressions, Operators, and Precedence

* sets - partial order, not total order. i.e.:

        >>> a
        {1, 2, 3}
        >>> b
        {4, 5, 6}
        >>> a < b or a >= b
        False

* chained assignment and chained comparisons - I didn't know you could do this!
        
        x = y = 3
        >>> 1 <= x + y <= 10
        True

    This means we don't have to compute `x + y` twice, like in the alternative:

        >>> 1 <= x + y and x + y <= 10
        True

* can I write a single python expression using every operator type listed in the operator precedence table?

## 1.5 - Functions

* This:
    
        >>> l = [1, 2, 3]
        >>> def foo(l):
        ...     l.append(4)
        ... 
        >>> foo(l)
        >>> l
        [1, 2, 3, 4]

## 1.8 - Iterators and Generators

* I made a for loop!

        >>> def for_loop(iterable):
        ...     try:
        ...             i = iter(iterable)
        ...             print(next(i))
        ...             for_loop(i)
        ...     except StopIteration:
        ...             pass
        ... 
        >>> for_loop('cat')
        c
        a
        t

    Or I could do it like this, which doesn't create a new iterator instance every time:

    >>> def for_loop(iterator):
    ...     try:
    ...             print(next(iterator))
    ...             for_loop(iterator)
    ...     except TypeError:
    ...             iterator = iter(iterator)
    ...             for_loop(iterator)
    ...     except StopIteration:
    ...             pass
    ... 

* Ah, iterators keep track of the index of the original iterable. So, if the original iterable is mutable, and you mutate it, the iterator reflects the changes:

        >>> l = list('i am a cat')
        >>> i = iter(l)
        >>> for j in range(len(l)):
        ...     if j % 2 == 0:
        ...             l[j] = j
        ...     print(next(i))
        ... 
        0
         
        2
        m
        4
        a
        6
        c
        8
        t

