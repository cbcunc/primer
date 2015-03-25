#! /usr/bin/env python

"""
Package of prime number objects.
"""


def prime_generator_function():
    """Return a generator for prime numbers."""

    p = [2, ]
    while True:
        yield p[-1]
        q = p[-1] + 1
        while True:
            for x in p:
                if not (q % x):
                    break
            else:
                p.append(q)
                break
            q += 1


pgf = prime_generator_function


def primes(n):
    """Return a sequence of the first n primes."""

    pg = pgf()
    return [pg.next() for x in range(n)]


def prime(n):
    """Return the nth prime."""

    return primes(n)[-1]


def primorial(n):
    """Return the nth primorial."""

    return reduce(lambda x, y: x * y, primes(n))
