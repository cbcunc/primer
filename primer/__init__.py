#! /usr/bin/env python

"""
Package of prime number objects.
"""


def _prime_generator_function():
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


_pgf = _prime_generator_function


def primes(n):
    """
    Return a sequence of the first n primes.

    primes(n) -> [2, 3, 5, ..., Pn]

    where Pn is the nth prime number.
    """

    pg = _pgf()
    return [pg.next() for x in range(n)]


def prime(n):
    """
    Return the nth prime.

    prime(n) -> Pn

    where Pn is the nth prime number.
    """

    return primes(n)[-1]


def primorial(n):
    """Return the nth primorial.

    primorial(n) -> Pn#

    where Pn# is the nth primorial number.
    """

    return reduce(lambda x, y: x * y, primes(n))
