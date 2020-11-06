def is_multiple(n, m):
    """ this function to check if n is multiple of m.
        return True if it is, else return false.
    """
    if n%m == 0:
        return True
    return False

#Ex: test with some input
print(is_multiple(2,2))
print(is_multiple(4,3))
print(is_multiple(8,4))

