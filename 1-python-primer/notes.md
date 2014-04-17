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

