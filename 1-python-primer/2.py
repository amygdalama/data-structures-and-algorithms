# not allowed to use multiplication, modulo, or division operators

def is_even_bitwise(k):
    return k & 1

def is_even_string(k):
    evens = {'0', '2', '4', '6', '8'}
    return str(k)[-1] in evens
