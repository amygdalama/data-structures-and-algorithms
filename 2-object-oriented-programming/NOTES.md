## 2.4 - Inheritance

* Protected/Private attributes:

        >>> class Foo():
        ...     __x = 1
        ...     _y = __x    
        ...     z = __x
        ... 
        >>> f = Foo()
        >>> f.__x
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'Foo' object has no attribute '__x'
        >>> f._y
        1
        >>> f.z
        1
        >>> f.__x = 5
        >>> f._y
        1
        >>> f.z
        1
